from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView
)

urlpatterns = [
    path('product/list', ProductListView.as_view()),
    path('product/create', ProductCreateView.as_view())
]