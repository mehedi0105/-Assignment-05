from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='books/media/uploads/', blank=True, null=True)
    borrow_price = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    borrow_date = models.DateField(default=timezone.now)
    borrow = models.BooleanField(default=False)
    def __str__(self):
        return self.book_name

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self}"