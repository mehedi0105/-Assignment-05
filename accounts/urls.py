from django.urls import path
from .views import UserRegistrationView, UserLoginView, user_logout, profile, UserInformationView, pass_change


urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    # path('profile/',profile,name='profile'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',user_logout,name='logout'),
    path('information_update/',UserInformationView.as_view(),name='profile_update'),
    path('pass_change/',pass_change,name='pass_change'),

]
