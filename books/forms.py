from django import forms
from .models import Book,Comment

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['writer']

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name','email','body']
        # exclude = ['author']