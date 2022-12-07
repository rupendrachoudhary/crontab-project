from django.urls import path, re_path
from . import views
from .views import HomeView, BlogView, ContactView, TermsView, PrivacyView, CookieView, MinuteView

urlpatterns = [
    path('',HomeView.as_view(), name="home"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('contact/',ContactView.as_view(), name="contact"),
    path('terms-and-conditions/',TermsView.as_view(), name="terms_condition"),
    path('privacy-policies/',PrivacyView.as_view(), name="privacy-policies"),
    path('cookie-policies/',CookieView.as_view(), name="cookie-policies"),
    re_path(r'^every-(?P<n>[0-5][0-9]?)-minutes/$',MinuteView.as_view(),name="minutes"),
    re_path(r'^every-minute/',HomeView.as_view(), name="everyminute"),
    re_path(r'^every-even-minute/',HomeView.as_view(), name="everyevenminute"),
    re_path(r'^every-odd-minute/',HomeView.as_view(), name="everyoddminute"),

    
    
   
]
