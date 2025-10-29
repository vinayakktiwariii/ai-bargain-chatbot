from django.core.management.base import BaseCommand
from products.models import Product


class Command(BaseCommand):
    help = 'Add sample products to database'

    def handle(self, *args, **kwargs):
        # Delete existing products
        Product.objects.all().delete()
        self.stdout.write(self.style.WARNING('Deleted existing products'))

        # Product 1: Nike Air Jordans
        Product.objects.create(
            name="Nike Air Jordans 1 Low",
            description="Premium basketball shoes with iconic design and superior comfort. Perfect for both court performance and street style.",
            image_url="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500",
            image_url_2="https://images.unsplash.com/photo-1552346154-21d32810aba3?w=500",
            list_price=10995,
            min_price=8995,
            auto_accept_threshold=10495,
            auto_decline_threshold=7995,
            max_rounds=5,
            concession_rate=0.5
        )

        # Product 2: Apple AirPods Pro
        Product.objects.create(
            name="Apple AirPods Pro",
            description="Active noise cancellation for immersive sound. Transparency mode for hearing surroundings. Wireless charging case included.",
            image_url="https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=500",
            image_url_2="https://images.unsplash.com/photo-1588423771073-b8903fbb85b5?w=500",
            list_price=24900,
            min_price=22000,
            auto_accept_threshold=24000,
            auto_decline_threshold=20000,
            max_rounds=5,
            concession_rate=0.5
        )

        # Product 3: MacBook Pro M3
        Product.objects.create(
            name="MacBook Pro M3 14-inch",
            description="Revolutionary M3 chip delivers exceptional performance and battery life. Liquid Retina XDR display for stunning visuals.",
            image_url="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500",
            image_url_2="https://images.unsplash.com/photo-1611186871348-b1ce696e52c9?w=500",
            list_price=169900,
            min_price=159900,
            auto_accept_threshold=167900,
            auto_decline_threshold=155000,
            max_rounds=4,
            concession_rate=0.3
        )

        # Product 4: Sony WH-1000XM5 Headphones
        Product.objects.create(
            name="Sony WH-1000XM5 Headphones",
            description="Industry-leading noise cancellation with exceptional sound quality. 30-hour battery life and premium comfort design.",
            image_url="https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=500",
            image_url_2="https://images.unsplash.com/photo-1484704849700-f032a568e944?w=500",
            list_price=29990,
            min_price=26000,
            auto_accept_threshold=29000,
            auto_decline_threshold=24000,
            max_rounds=5,
            concession_rate=0.5
        )

        # Product 5: Canon EOS R6 Camera
        Product.objects.create(
            name="Canon EOS R6 Mirrorless Camera",
            description="Professional full-frame mirrorless camera with 20MP sensor and advanced autofocus. Perfect for photography enthusiasts.",
            image_url="https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=500",
            image_url_2="https://images.unsplash.com/photo-1606941923511-69e4c42e8b5f?w=500",
            list_price=219900,
            min_price=205000,
            auto_accept_threshold=215900,
            auto_decline_threshold=200000,
            max_rounds=4,
            concession_rate=0.4
        )

        # Product 6: Samsung Galaxy Watch 6
        Product.objects.create(
            name="Samsung Galaxy Watch 6",
            description="Advanced health tracking with heart rate monitoring, sleep tracking, and fitness features. Premium AMOLED display.",
            image_url="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500",
            image_url_2="https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=500",
            list_price=27999,
            min_price=24000,
            auto_accept_threshold=27000,
            auto_decline_threshold=22000,
            max_rounds=5,
            concession_rate=0.5
        )

        # Product 7: PlayStation 5
        Product.objects.create(
            name="Sony PlayStation 5 Console",
            description="Next-gen gaming console with lightning-fast loading and stunning graphics. Includes DualSense wireless controller.",
            image_url="https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=500",
            image_url_2="https://images.unsplash.com/photo-1622297845775-5ff3fef71d13?w=500",
            list_price=49990,
            min_price=46000,
            auto_accept_threshold=49000,
            auto_decline_threshold=44000,
            max_rounds=4,
            concession_rate=0.4
        )

        self.stdout.write(self.style.SUCCESS('\n✅ Successfully created 7 products!'))
        
        # List products
        self.stdout.write('\nProducts:')
        for product in Product.objects.all():
            self.stdout.write(f'  - {product.name} (₹{product.list_price})')
