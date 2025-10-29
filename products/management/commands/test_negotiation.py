"""
Django management command to test the negotiation algorithm
Usage: python manage.py test_negotiation
"""

"""
Django management command to test the negotiation algorithm
Usage: python manage.py test_negotiation
"""

from django.core.management.base import BaseCommand
from products.models import Product
from chat.negotiation_engine import simulate_negotiation


class Command(BaseCommand):
    help = 'Test the negotiation algorithm with sample scenarios'

    def handle(self, *args, **options):
        # Get first product or create a test one
        product = Product.objects.first()
        
        if not product:
            self.stdout.write(self.style.ERROR('No products found! Add one in admin first.'))
            return
        
        self.stdout.write(self.style.SUCCESS(f'\nTesting with product: {product.name}\n'))
        
        # Calculate realistic test offers based on product price
        list_price = float(product.list_price)
        min_price = float(product.min_price)
        auto_accept = float(product.auto_accept_threshold)
        
        # Scenario 1: User starts below min and gradually increases
        self.stdout.write(self.style.WARNING('\n📍 SCENARIO 1: Starting Below Minimum'))
        low_offer1 = min_price * 0.85  # 15% below min
        low_offer2 = min_price * 0.90  # 10% below min
        low_offer3 = min_price * 0.95  # 5% below min
        simulate_negotiation(product, [low_offer1, low_offer2, low_offer3])
        
        # Scenario 2: User starts in negotiation zone
        self.stdout.write(self.style.WARNING('\n📍 SCENARIO 2: Normal Negotiation'))
        mid_offer1 = list_price * 0.75  # 25% off list
        mid_offer2 = list_price * 0.82  # 18% off list
        mid_offer3 = list_price * 0.88  # 12% off list
        simulate_negotiation(product, [mid_offer1, mid_offer2, mid_offer3])
        
        # Scenario 3: User starts high (auto-accept)
        self.stdout.write(self.style.WARNING('\n📍 SCENARIO 3: High Offer (Auto-Accept)'))
        high_offer = auto_accept + 100  # Above auto-accept threshold
        simulate_negotiation(product, [high_offer])
        
        # Scenario 4: User starts very low (auto-decline)
        self.stdout.write(self.style.WARNING('\n📍 SCENARIO 4: Too Low (Auto-Decline)'))
        very_low = min_price * 0.50  # 50% of minimum
        simulate_negotiation(product, [very_low])
        
        # Scenario 5: Strategic negotiation
        self.stdout.write(self.style.WARNING('\n📍 SCENARIO 5: Strategic Buyer'))
        strat1 = list_price * 0.80  # Start at 20% off
        strat2 = list_price * 0.85  # Move to 15% off
        strat3 = list_price * 0.90  # Final at 10% off
        simulate_negotiation(product, [strat1, strat2, strat3])
        
        self.stdout.write(self.style.SUCCESS('\n✅ All scenarios tested!\n'))
