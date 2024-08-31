from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BookModel(models.Model):
    title =  models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn =  models.CharField(max_length=100, unique=True)
    copies_available = models.IntegerField(default=1)
    added = models.DateField(auto_now=True)

    def __str__(self):
        return self.title




class BookRental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rental") # user
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name="rental")
    rented_on = models.DateField(auto_now_add=True)
    returned_on = models.DateField(blank=True, null= True)


