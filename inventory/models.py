from django.db import models
from rest_framework.serializers import ValidationError

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        unique_together = ('product', 'warehouse')

    def __str__(self):
        return f'{self.product.name} in {self.warehouse.name} - {self.quantity}'


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Update Stock on Purchase
        stock, created = Stock.objects.get_or_create(product=self.product, warehouse=self.warehouse)
        stock.quantity += self.quantity
        stock.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Purchased {self.quantity} of {self.product.name} for {self.warehouse.name}'


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Update Stock on Sale
        stocks = Stock.objects.get(product=self.product, warehouse=self.warehouse)
        for stock in stocks:
            if stock.quantity >= self.quantity:
                stock.quantity -= self.quantity
                stock.save()
                super().save(*args, **kwargs)
        else:
            raise ValidationError({"details": "not enough stock available"})

    def __str__(self):
        return f'Sold {self.quantity} of {self.product.name} from {self.warehouse.name}'
