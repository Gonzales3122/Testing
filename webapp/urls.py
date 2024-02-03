from django.urls import path
from .views import index, about, contact, services, reservation_view, success
from . import views

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('reservation/', reservation_view, name='reservation_view'),
    path('success/', success, name='success'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('reservations/new/', views.reservation_create, name='reservation_create'),
    path('reservations/<int:pk>/edit/', views.reservation_update, name='reservation_update'),
    path('reservations/<int:pk>/delete/', views.reservation_delete, name='reservation_delete'),
    
]
