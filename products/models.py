from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    # Main image
    image_url = models.URLField(blank=True)
    
    # Additional images (comma-separated URLs)
    image_url_2 = models.URLField(blank=True, verbose_name="Image 2")
    image_url_3 = models.URLField(blank=True, verbose_name="Image 3")
    image_url_4 = models.URLField(blank=True, verbose_name="Image 4")
    
    # Pricing strategy
    list_price = models.DecimalField(max_digits=10, decimal_places=2)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    auto_accept_threshold = models.DecimalField(max_digits=10, decimal_places=2)
    auto_decline_threshold = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Negotiation settings
    max_rounds = models.IntegerField(default=3)
    concession_rate = models.FloatField(default=0.5)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def get_all_images(self):
        """Return list of all available image URLs"""
        images = [self.image_url]
        if self.image_url_2:
            images.append(self.image_url_2)
        if self.image_url_3:
            images.append(self.image_url_3)
        if self.image_url_4:
            images.append(self.image_url_4)
        return [img for img in images if img]
    
    class Meta:
        ordering = ['-created_at']
