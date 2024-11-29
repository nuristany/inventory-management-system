from rest_framework import serializers
from .models import Product, Warehouse, Stock, Purchase, Sale

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Warehouse Serializer
class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

# Stock Serializer
class StockSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    warehouse_name = serializers.CharField(source='warehouse.name', read_only=True)
    warehouse_location = serializers.CharField(source='warehouse.location', read_only=True)

    class Meta:
        model = Stock
        fields = ['id', 'product', 'product_name', 'warehouse', 'warehouse_name', 'quantity', 'warehouse_location']

# Purchase Serializer
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

# Sale Serializer
class SaleSerializer(serializers.ModelSerializer):
    sales = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Sale
        fields = '__all__'
