from django.db import models
from products.models import Products


class Order(models.Model):

    full_name = models.CharField(max_length=200)

    address = models.TextField()

    phone = models.CharField(max_length=20)

    total_price = models.FloatField()

    is_paid = models.BooleanField(default=False)

    razorpay_order_id = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    razorpay_payment_id = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    razorpay_signature = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(default=1)

    price = models.FloatField()

    def __str__(self):
        return self.product.name