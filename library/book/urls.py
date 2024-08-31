from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, RentalViewSet

router = DefaultRouter()

router.register(r"book", BookViewSet, basename = "book")   
router.register(r"", RentalViewSet, basename = "rental")


urlpatterns = [
    path('', include(router.urls)),  
]