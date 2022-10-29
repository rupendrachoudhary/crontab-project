from django.urls import path
from . import views
from .views import HomeView, BlogView, ContactView, TermsView, PrivacyView, CookieView

urlpatterns = [
    path('',HomeView.as_view(), name="home"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('contact/',ContactView.as_view(), name="contact"),
    path('terms-and-conditions/',TermsView.as_view(), name="terms_condition"),
    path('privacy-policies/',PrivacyView.as_view(), name="privacy-policies"),
    path('cookie-policies/',CookieView.as_view(), name="cookie-policies"),
    
   
]
