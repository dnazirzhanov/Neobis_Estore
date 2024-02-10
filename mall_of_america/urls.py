from django.contrib import admin
from django.urls import path, include
from .views import ProductAPIView, ProductDetailAPIView, OrderProduct, MakeComment

urlpatterns = [
    path('api/product/', ProductAPIView.as_view(), name='product-list-or-create'),
    path('api/product/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('api/order/', OrderProduct.as_view(), name='product-detail'),
    path('api/comments/', MakeComment.as_view(), name='product-list-or-create'),
]
