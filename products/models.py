from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)

    desc = models.TextField()

    def __str__(self):
        return self.name


class Products(models.Model):

    name = models.CharField(max_length=100)

    desc = models.TextField()

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(default=1)

    price = models.FloatField()

    # STATIC IMAGE PATH
    image = models.CharField(max_length=200)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name