import uuid
from django.db import models
from product.models import TimeStampModel, Product
from django.conf import settings


class Cart(TimeStampModel):
    uuid = models.UUIDField(default=uuid.uuid4)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    amount_to_be_paid = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    is_checked_out = models.BooleanField(default=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="carts"
    )

    def __str__(self):
        return str(self.uuid)



class CartItem(TimeStampModel):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cartitems"
    )

    def __str__(self):
        return f"{self.product} -> {self.unit_price}"

    def save(self, *args, **kwargs):
        self.total_price = self.unit_price * self.quantity
        super().save(*args, **kwargs)

