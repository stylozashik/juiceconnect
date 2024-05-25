from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    UNIT_CHOICES = [
        (60, '60ml'),
        (100, '100ml'),
        (120, '120ml'),
    ]
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    long_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/product_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.IntegerField(choices=UNIT_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title
