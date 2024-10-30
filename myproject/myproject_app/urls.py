from django.urls import path
from . import views
from .views import services

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about_me', views.about_me, name = 'about_me'),
    path('projects', views.projects, name = 'projects'),
    path('image', views.image, name = 'image'),
    path('contact_me', views.contact_me, name = 'contact_me'),
    path('services', views.services, name = 'services'),
    path('buy', views.buy, name = 'buy'),
    path('order_done', views.order_done, name = 'order_done'),
    
]