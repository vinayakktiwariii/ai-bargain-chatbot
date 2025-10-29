from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
from chat.negotiation_engine import NegotiationEngine
import json
import logging

logger = logging.getLogger(__name__)

# Store sessions in memory (for development)
# Key: session_id, Value: NegotiationEngine instance
active_sessions = {}

@csrf_exempt
def negotiate(request, product_id):
    """Handle negotiation via HTTP POST"""
    
    if request.method == 'GET':
        # Initialize session
        try:
            product = Product.objects.get(pk=product_id)
            return JsonResponse({
                'success': True,
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'list_price': float(product.list_price),
                    'min_price': float(product.min_price)
                },
                'message': f"Welcome! Let's negotiate on {product.name}. The asking price is ₹{product.list_price}. What's your offer?"
            })
        except Product.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Product not found'}, status=404)
    
    elif request.method == 'POST':
        try:
            # Parse request data
            data = json.loads(request.body)
            user_offer = float(data.get('amount'))
            session_id = data.get('session_id', f'session_{product_id}')
            
            logger.info(f"Session: {session_id}, Offer: ₹{user_offer}")
            
            # Get or create negotiation engine for this session
            if session_id not in active_sessions:
                product = Product.objects.get(pk=product_id)
                active_sessions[session_id] = NegotiationEngine(product)
                logger.info(f"Created new engine for {session_id}")
            
            engine = active_sessions[session_id]
            
            # Process the offer
            result = engine.process_offer(user_offer)
            
            logger.info(f"Result: {result['action']} at ₹{result['price']}, Round {result['round']}")
            
            # Get stats
            stats = engine.get_negotiation_stats()
            
            # Clean up session if negotiation ended
            if result.get('is_final') and result['action'] in ['accept', 'decline']:
                logger.info(f"Cleaning up session {session_id}")
                # Keep session for a bit in case user refreshes
                # del active_sessions[session_id]
            
            return JsonResponse({
                'success': True,
                'result': result,
                'stats': stats
            })
            
        except Product.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Product not found'}, status=404)
        except ValueError as e:
            logger.error(f"Invalid offer amount: {e}")
            return JsonResponse({'success': False, 'error': 'Invalid offer amount'}, status=400)
        except Exception as e:
            logger.error(f"Negotiation error: {e}")
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    
    return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)
