
from django.urls import path
from .views import Add_Category
urlpatterns = [
    path('add_category/', Add_Category, name='add_category')
]