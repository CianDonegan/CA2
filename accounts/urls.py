from django.urls import path
from shop import views
from .views import aboutUs, contactUs, signupView, signinView, signoutView

urlpatterns = [
    path('create/', signupView, name='signup'),
    path('login/', signinView, name='signin'),
    path('logout/', signoutView, name='signout'),
    path('contactus/', contactUs, name='contact'),
    path('aboutus/', aboutUs, name="aboutus")
]