from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(TimeStampModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Brand(TimeStampModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Status(models.TextChoices):
    DRAFT = "draft", "DRAFT"
    PUBLISH = "publish", "PUBLISH"
    BLOCKED = "blocked", "BLOCKED"


class Product(TimeStampModel):
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=255)
    marked_price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    display_price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="product/images", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.DRAFT)

    def __str__(self):
        return f"{self.name}({self.sku})"

    def save(self, *args, **kwargs):
        mp = self.marked_price
        dis = self.discount
        self.display_price = mp - (dis/100 * mp)
        super().save(*args, **kwargs)

