from re import I
from django.urls import path
from rest_framework import urlpatterns
from .views import UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()

router.register('user', UserViewSet, basename='user')
urlpatterns = router.urls


