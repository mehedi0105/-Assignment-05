from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('add_book/',views.AddPostView.as_view(), name='add_post'),
    path('details/<int:id>/', views.DetailsPostView.as_view(), name='details_post'),
    path('Brrow_Book/<int:id>/', views.Brrow_Book, name='Brrow_Book'),
    path('return_Book/<int:id>/', views.Return_Book, name='return_Book'),
     path('comment_post/<int:id>', views.CommentPostView.as_view(), name='comment_post'),
    # path('details_post/<int:id>', views.DetailsPostView.as_view(), name='details_post'),
]
