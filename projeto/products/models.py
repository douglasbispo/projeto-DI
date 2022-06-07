from django.db import models
import uuid

# Create your models here.
def product_image_name(instance, filename):
    return f"{instance.name}-{str(uuid.uuid4())}-{filename}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=19, decimal_places=2)
    validity = models.DateField()
    image = models.ImageField(upload_to=product_image_name)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
