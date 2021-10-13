from re import I
from django.db.models.query_utils import Q
from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)
from products.serializers import ProductSerializer, ProductListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from products.models import Product


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', ]


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductSerializer

