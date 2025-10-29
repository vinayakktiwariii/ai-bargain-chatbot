"""
Bargaining Algorithm - The core negotiation logic
Based on alternating-offer bargaining models with bounded concessions
"""

from decimal import Decimal
from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)


class NegotiationEngine:
    """
    Handles price negotiation logic using game-theory-inspired rules.
    Features:
    - Auto-accept/decline thresholds
    - Progressive concessions
    - Round limits
    - Smart acceptance of good offers
    """
    
    def __init__(self, product, max_rounds: int = 5):
        """
        Initialize negotiation for a product.
        
        Args:
            product: Product model instance
            max_rounds: Maximum negotiation rounds (default: 5)
        """
        self.product = product
        self.list_price = Decimal(str(product.list_price))
        self.min_price = Decimal(str(product.min_price))
        self.auto_accept = Decimal(str(product.auto_accept_threshold))
        self.auto_decline = Decimal(str(product.auto_decline_threshold))
        self.max_rounds = max_rounds
        self.concession_rate = float(product.concession_rate)
        
        # Track negotiation state
        self.current_round = 0
        self.last_bot_offer = None  # Track bot's last counteroffer
        self.history = []
        
        logger.info(f"Initialized - List: ₹{self.list_price}, Min: ₹{self.min_price}, Accept: ₹{self.auto_accept}, Decline: ₹{self.auto_decline}")
        
    def process_offer(self, user_offer: float) -> Dict:
        """
        Process user's offer and return bot's decision.
        
        Args:
            user_offer: User's proposed price
            
        Returns:
            Dict with keys: action, price, message, round, is_final
        """
        user_offer = Decimal(str(user_offer))
        self.current_round += 1
        
        # Log the offer
        self.history.append({
            'round': self.current_round,
            'user_offer': float(user_offer),
            'timestamp': 'now'
        })
        
        logger.info(f"Round {self.current_round}: User offered ₹{user_offer}")
        logger.info(f"Last bot offer: ₹{self.last_bot_offer}")
        
        # CRITICAL: Accept if user meets or exceeds bot's last offer
        if self.last_bot_offer and user_offer >= self.last_bot_offer:
            logger.info(f"✅ User accepted our offer!")
            return self._accept_offer(user_offer)
        
        # Rule 1: Auto-accept if offer is at or above auto-accept threshold
        if user_offer >= self.auto_accept:
            logger.info(f"✅ Auto-accepting (offer >= auto_accept)")
            return self._accept_offer(user_offer)
        
        # Rule 2: Auto-decline if offer is too low
        if user_offer < self.auto_decline:
            logger.info(f"❌ Auto-declining (offer < auto_decline)")
            return self._decline_offer(user_offer)
        
        # Rule 3: Accept if offer is above min price and close to bot's target
        if user_offer >= self.min_price:
            # If user is within 5% of min price, accept it
            threshold = self.min_price * Decimal('1.05')
            if user_offer >= threshold:
                logger.info(f"✅ Accepting good offer (above min + 5%)")
                return self._accept_offer(user_offer)
        
        # Rule 4: Check if we've reached max rounds
        if self.current_round >= self.max_rounds:
            logger.info(f"⏰ Max rounds reached")
            return self._final_offer(user_offer)
        
        # Rule 5: Make a counteroffer
        logger.info(f"💬 Making counteroffer")
        return self._counter_offer(user_offer)
    
    def _accept_offer(self, price: Decimal) -> Dict:
        """Accept the user's offer"""
        logger.info(f"✅ ACCEPTED at ₹{price}")
        return {
            'action': 'accept',
            'price': float(price),
            'message': f"Deal! I accept your offer of ₹{price}. Let's complete the purchase! 🎉",
            'round': self.current_round,
            'is_final': True,
            'show_buttons': False
        }
    
    def _decline_offer(self, price: Decimal) -> Dict:
        """Decline the user's offer"""
        logger.info(f"❌ DECLINED ₹{price} (too low)")
        return {
            'action': 'decline',
            'price': float(self.min_price),
            'message': f"I'm sorry, ₹{price} is too low for this premium product. "
                      f"I can't go below ₹{self.min_price}. Would you consider a higher offer?",
            'round': self.current_round,
            'is_final': False,
            'show_buttons': False
        }
    
    def _counter_offer(self, user_offer: Decimal) -> Dict:
        """Calculate and return a counteroffer"""
        # Progressive concession: become more generous each round
        round_factor = 1 + (self.current_round * 0.2)  # 20% more generous per round
        effective_concession = min(0.95, self.concession_rate * round_factor)
        
        # Calculate target price (moving toward user's offer)
        price_gap = self.list_price - user_offer
        concession_amount = price_gap * Decimal(str(effective_concession))
        target_price = self.list_price - concession_amount
        
        # Enforce floor price
        counter_price = max(self.min_price, target_price)
        
        # Round to nearest 10
        counter_price = (counter_price / 10).quantize(Decimal('1')) * 10
        
        # Store this offer
        self.last_bot_offer = counter_price
        
        logger.info(f"💬 COUNTER at ₹{counter_price}")
        
        # Craft message based on how close we're getting
        discount_pct = ((self.list_price - counter_price) / self.list_price) * 100
        
        if discount_pct > 15:
            tone = "That's a great offer! I can do"
        elif discount_pct > 10:
            tone = "Getting closer! How about"
        else:
            tone = "I can meet you at"
        
        return {
            'action': 'counter',
            'price': float(counter_price),
            'message': f"{tone} ₹{counter_price}? That's {int(discount_pct)}% off! 💰",
            'round': self.current_round,
            'is_final': False,
            'show_buttons': False
        }
    
    def _final_offer(self, user_offer: Decimal) -> Dict:
        """Give final offer when max rounds reached"""
        # Calculate best possible price (most generous)
        final_price = max(self.min_price, user_offer * Decimal('1.08'))  # Meet 92% of the way
        final_price = min(final_price, self.list_price)
        
        # Round to nearest 50
        final_price = (final_price / 50).quantize(Decimal('1')) * 50
        
        # Store this offer
        self.last_bot_offer = final_price
        
        logger.info(f"⏰ FINAL OFFER at ₹{final_price}")
        
        return {
            'action': 'final',
            'price': float(final_price),
            'message': f"This is my absolute final offer: ₹{final_price}. Accept or decline?",
            'round': self.current_round,
            'is_final': True,
            'show_buttons': True  # Show Accept/Decline buttons
        }
    
    def get_negotiation_stats(self) -> Dict:
        """Return statistics about the negotiation"""
        if not self.history:
            return {}
        
        offers = [h['user_offer'] for h in self.history]
        return {
            'total_rounds': self.current_round,
            'starting_offer': offers[0] if offers else 0,
            'latest_offer': offers[-1] if offers else 0,
            'average_offer': sum(offers) / len(offers) if offers else 0,
            'list_price': float(self.list_price),
            'min_price': float(self.min_price)
        }
