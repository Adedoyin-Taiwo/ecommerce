import uuid

from django.contrib.auth.models import User
from django.db import models

from utils.generate_id import generate_id
from utils.model_base import Base


class Product(Base):
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    image = models.FileField(upload_to="products")

    def __str__(self):
        return self.product_name


class OrderedProduct(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveIntegerField(default=1)

    def get_final_price(self):
        return self.quantity * self.product.product_price


class Order(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_product = models.ManyToManyField(OrderedProduct)
    order_id = models.CharField(max_length=12, default=generate_id, unique=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-created_at']

    def get_total(self):
        total = 0
        for item in self.ordered_product.all():
            total += item.get_final_price()
            return float(total)



