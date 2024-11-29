from django.urls import path
from .views import (
    ProductListCreateView,
    ProductDetailView,
    WarehouseListCreateView,
    WarehouseDetailView,
    StockListView,
    StockByProductView,
    PurchaseCreateView,
    SaleCreateView,
)

urlpatterns = [
    # Product URLs
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Warehouse URLs
    path('warehouses/', WarehouseListCreateView.as_view(), name='warehouse-list-create'),
    path('warehouses/<int:pk>/', WarehouseDetailView.as_view(), name='warehouse-detail'),

    # Stock URLs
    path('stocks/', StockListView.as_view(), name='stock-list'),
    path('stocks/product/<int:product_id>/', StockByProductView.as_view(), name='stock-by-product'),

    # Purchase URLs
    path('purchases/', PurchaseCreateView.as_view(), name='purchase-create'),

    # Sale URLs
    path('sales/', SaleCreateView.as_view(), name='sale-create'),
]
