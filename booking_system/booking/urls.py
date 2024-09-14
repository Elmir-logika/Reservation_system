from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.room_list_view, name='room_list'),  # Відображення всіх кімнат
    path('booking/', views.booking_create_view, name='booking_create'),  # Форма для бронювання
    path('booking/success/', views.booking_success_view, name='booking_success'),  # Повідомлення про успішне бронювання
]