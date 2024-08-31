from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .models import BookRental, BookModel
from .serializers import BookSerializer, RentalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone

# Book ViewSet
class BookViewSet(ViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    Response(serializer_class)

# Rental ViewSet
class RentalViewSet(ViewSet):
    # queryset = BookRental.objects.all()
    # serializer_class = RentalSerializer
    # permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['post'], url_path="rent")
    def perform_create(self, request):
        #user = self.request.user
        data = request.data
        user_id = data.get("id")
        title = data.get('title')
        author = data.get('author')
        isbn = data.get('isbn')
        copies_available = data.get('copies_available', 1) 

        print(request.data, "check data here.....")
        

        # Check if the book is available
        # if book.copies_available > 0:
        #     # Check if the user has already rented this book and hasn't returned it
        #     if not BookRental.objects.filter(user=user, book=book, returned_on__isnull=True).exists():
        #         # Decrease the number of available copies
        #         book.copies_available -= 1
        #         book.save()
        #         serializer.save(user=user)
        #     else:
        #         raise serializers.ValidationError("You have already rented this book.")
        # else:
        #     raise serializers.ValidationError("This book is currently not available.")

    # @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    # def return_book(self, request, pk=None):
    #     print(request.data)
    #     rental = self.get_object()
        
    #     # Check if the book has already been returned
    #     if rental.returned_on is None:
    #         # Mark the book as returned
    #         rental.returned_on = timezone.now()
    #         rental.book.copies_available += 1
    #         rental.book.save()
    #         rental.save()
    #         return Response({"status": "Book returned"}, status=status.HTTP_200_OK)
    #     return Response({"error": "Book already returned"}, status=status.HTTP_400_BAD_REQUEST)
