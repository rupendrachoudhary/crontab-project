from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="cronapp-home"),
    path('blog/', views.blog, name="cronapp-blog"),
    path('contact/',views.contact, name="cronapp-contact")

]
