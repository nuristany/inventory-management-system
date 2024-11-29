from rest_framework import generics, status
from rest_framework.response import Response
from .models import Product, Warehouse, Stock, Purchase, Sale
from .serializers import (
    ProductSerializer,
    WarehouseSerializer,
    StockSerializer,
    PurchaseSerializer,
    SaleSerializer,
)

# Product Views
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Warehouse Views
class WarehouseListCreateView(generics.ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class WarehouseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

# Stock Views
class StockListView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockByProductView(generics.ListAPIView):
    serializer_class = StockSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Stock.objects.filter(product_id=product_id)

# Purchase Views
class PurchaseCreateView(generics.CreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

# Sale Views
class SaleCreateView(generics.CreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
