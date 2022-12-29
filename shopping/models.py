import uuid
from django.db import models
from product.models import TimeStampModel, Product


class Cart(TimeStampModel):
    products = models.ManyToManyField(Product, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
