from django.db import models

# Create your models here.
from django.db import models
from products.models import Products


class Cart(models.Model):

    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(default=1)

    added_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.product.price * self.quantity