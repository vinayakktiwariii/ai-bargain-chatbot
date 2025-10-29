from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Load 15 premium products with real professional images'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        
        products = [
            {
                'name': 'Nike Air Jordan 1 Retro High',
                'description': 'Iconic basketball sneakers with premium leather construction. Features Air-Sole cushioning and classic colorway. Perfect for collectors and sneaker enthusiasts.',
                'image_url': 'https://images.pexels.com/photos/1598505/pexels-photo-1598505.jpeg?auto=compress&cs=tinysrgb&w=800',
                'list_price': 14995,
                'min_price': 12995,
                'auto_accept_threshold': 14495,
                'auto_decline_threshold': 11995,
            },
            {
                'name': 'Apple AirPods Pro 2nd Gen',
                'description': 'Active Noise Cancellation with Adaptive Transparency mode. Personalized Spatial Audio with dynamic head tracking. Up to 6 hours listening time with ANC enabled.',
                'image_url': 'https://images.pexels.com/photos/8000618/pexels-photo-8000618.jpeg?auto=compress&cs=tinysrgb&w=800',
                'list_price': 24900,
                'min_price': 22900,
                'auto_accept_threshold': 24400,
                'auto_decline_threshold': 21900,
            },
            {
                'name': 'Sony WH-1000XM5 Wireless Headphones',
                'description': 'Industry-leading noise cancellation with two processors. 30-hour battery life. Premium sound quality with LDAC and DSEE Extreme. Lightweight design.',
                'image_url': 'https://images.pexels.com/photos/3394650/pexels-photo-3394650.jpeg?auto=compress&cs=tinysrgb&w=800',
                'list_price': 34990,
                'min_price': 31990,
                'auto_accept_threshold': 33990,
                'auto_decline_threshold': 29990,
            },
            {
                'name': 'Samsung Galaxy Watch 6 Classic',
                'description': 'Advanced health monitoring with ECG and blood pressure. Rotating bezel for easy navigation. 5ATM water resistance. Sapphire crystal display.',
                'image_url': 'https://images.pexels.com/photos/393047/pexels-photo-393047.jpeg?auto=compress&cs=tinysrgb&w=800',
                'list_price': 39999,
                'min_price': 36999,
                'auto_accept_threshold': 38999,
                'auto_decline_threshold': 34999,
            },
            {
                'name': 'Sony PlayStation 5 Console',
                'description': 'Next-generation gaming with ultra-high-speed SSD. Ray tracing support. 4K gaming at 120Hz. Includes DualSense wireless controller with haptic feedback.',
                'image_url': 'https://images.pexels.com/photos/14391329/pexels-photo-14391329.jpeg?auto=compress&cs=tinysrgb&w=800',
                'list_price': 54990,
                'min_price': 51990,
                'auto_accept_threshold': 53990,
                'auto_decline_threshold': 49990,
            },
            {
                'name': 'Apple MacBook Pro 14" M3 Pro',
                'description': 'Revolutionary M3 Pro chip with 12-core CPU. 14.2-inch Liquid Retina XDR display. Up to 18 hours battery life. 16GB unified memory, 512GB SSD.',
                'image_url': 'https://images.pexels.com/photos/7974/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=800',
                'list_price': 199900,
                'min_price': 189900,
                'auto_accept_threshold': 197900,
                'auto_decline_threshold': 184900,
            },
            {
                'name': 'Canon EOS R6 Mark II Mirrorless',
                'description': 'Professional 24.2MP full-frame sensor. 40fps continuous shooting. 4K 60p video recording. Advanced Dual Pixel CMOS AF II with subject detection.',
                'image_url': 'https://images.pexels.com/photos/90946/pexels-photo-90946.jpeg?auto=compress&cs=tinysrgb&w=800',
                'list_price': 249900,
                'min_price': 239900,
                'auto_accept_threshold': 247900,
                'auto_decline_threshold': 234900,
            },
            {
                'name': 'DJI Mavic 3 Pro Cine',
                'description': 'Professional triple-camera system with Hasselblad. 43-minute flight time. Omnidirectional obstacle sensing. 8K video recording with 1TB SSD.',
                'image_url': 'https://images.pexels.com/photos/2876511/pexels-photo-2876511.jpeg?auto=compress&cs=tinysrgb&w=800',
                'list_price': 349900,
                'min_price': 339900,
                'auto_accept_threshold': 347900,
                'auto_decline_threshold': 334900,
            },
            {
                'name': 'Apple iPad Pro 12.9" M2',
                'description': 'Powerful M2 chip with 8-core CPU. 12.9-inch Liquid Retina XDR display with ProMotion. 5G cellular. Works with Apple Pencil 2nd gen and Magic Keyboard.',
                'image_url': 'https://images.pexels.com/photos/1334597/pexels-photo-1334597.jpeg?auto=compress&cs=tinysrgb&w=800',
                'list_price': 124900,
                'min_price': 119900,
                'auto_accept_threshold': 123400,
                'auto_decline_threshold': 116900,
            },
            {
                'name': 'Bose QuietComfort Ultra Earbuds',
                'description': 'World-class noise cancellation. CustomTune technology. Immersive audio with Bose Spatial Audio. 6-hour battery life with charging case.',
                'image_url': 'https://images.pexels.com/photos/3780681/pexels-photo-3780681.jpeg?auto=compress&cs=tinysrgb&w=800',
                'list_price': 29900,
                'min_price': 27900,
                'auto_accept_threshold': 29400,
                'auto_decline_threshold': 26900,
            },
            {
                'name': 'LG OLED evo C3 65-inch 4K TV',
                'description': 'Self-lit OLED pixels deliver perfect blacks. α9 AI Processor Gen6. 120Hz refresh rate. Dolby Vision IQ and Dolby Atmos. webOS smart platform.',
                'image_url': 'https://images.pexels.com/photos/1201996/pexels-photo-1201996.jpeg?auto=compress&cs=tinysrgb&w=800',
                'list_price': 189900,
                'min_price': 179900,
                'auto_accept_threshold': 187900,
                'auto_decline_threshold': 174900,
            },
            {
                'name': 'Dyson V15 Detect Absolute',
                'description': 'Laser reveals invisible dust. LCD screen shows real-time particle count. Up to 60 minutes runtime. Advanced filtration captures 99.99% of particles.',
                'image_url': 'https://images.pexels.com/photos/38325/vacuum-cleaner-carpet-cleaner-housework-38325.jpeg?auto=compress&cs=tinysrgb&w=800',
                'list_price': 74900,
                'min_price': 69900,
                'auto_accept_threshold': 73900,
                'auto_decline_threshold': 67900,
            },
            {
                'name': 'Instant Pot Duo Plus 9-in-1',
                'description': 'Multi-use pressure cooker, slow cooker, rice cooker, steamer, sauté pan, yogurt maker, warmer, sterilizer, and sous vide. 6-quart capacity.',
                'image_url': 'https://images.pexels.com/photos/4518843/pexels-photo-4518843.jpeg?auto=compress&cs=tinysrgb&w=800',
                'list_price': 12999,
                'min_price': 10999,
                'auto_accept_threshold': 12499,
                'auto_decline_threshold': 9999,
            },
            {
                'name': 'Herman Miller Aeron Chair Remastered',
                'description': 'Ergonomic office chair with PostureFit SL support. 8Z Pellicle mesh. Adjustable lumbar support. Tilt limiter and seat angle adjustment. 12-year warranty.',
                'image_url': 'https://images.pexels.com/photos/276583/pexels-photo-276583.jpeg?auto=compress&cs=tinysrgb&w=800',
                'list_price': 159900,
                'min_price': 149900,
                'auto_accept_threshold': 157900,
                'auto_decline_threshold': 144900,
            },
            {
                'name': 'Nespresso Vertuo Next Coffee Maker',
                'description': 'One-touch Centrifusion brewing technology. Brews 5 cup sizes from espresso to carafe. Automatic blend recognition. Sustainable made from 54% recycled plastic.',
                'image_url': 'https://images.pexels.com/photos/851555/pexels-photo-851555.jpeg?auto=compress&cs=tinysrgb&w=800',
                'list_price': 19900,
                'min_price': 17900,
                'auto_accept_threshold': 19400,
                'auto_decline_threshold': 16900,
            },
        ]

        for data in products:
            Product.objects.create(**data)
            self.stdout.write(f'✓ Created: {data["name"]}')

        self.stdout.write(self.style.SUCCESS(f'\n🎉 Successfully loaded {len(products)} premium products!'))
