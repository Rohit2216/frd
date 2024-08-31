from rest_framework import serializers
from .models import BookModel, BookRental


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= BookModel
        fields= "__all__"


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model= BookRental
        fields= "__all__"


