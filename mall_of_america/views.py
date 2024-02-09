from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .models import Product, Order, Category, Comment
from .serializers import ProductSerializer, OrderSerializer, CategorySerializer, CommentSerializer

class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderProduct(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class MakeComment(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

