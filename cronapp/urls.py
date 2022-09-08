from django.urls import path
from . import views
from .views import HomeView, BlogView, ContactView

urlpatterns = [
    path('',HomeView.as_view(), name="home"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('contact/',ContactView.as_view(), name="contact"),
    
   
]
