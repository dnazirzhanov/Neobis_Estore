from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    sale = models.IntegerField(default=0, help_text="Enter a discount in percents (%)")

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.id} made by {self.user.username}"

    def calculate_total_price(self):
        price_with_discount = float(self.product.price) * (1 - (self.product.sale / 100))
        return Decimal(price_with_discount) * self.quantity
    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_price()
        super(Order, self).save(*args, **kwargs)

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    time_comment_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user} left a comment on this product: {self.product.name}"



