from django.shortcuts import render, redirect
from django.db.models import Q

def is_room_available(room, start_time, end_time):
    # доступна ли комната на указанный период времени
    conflicting_bookings = Booking.objects.filter(
        Q(room=room) & 
        (Q(start_time__lt=end_time) & Q(end_time__gt=start_time))
    )
    return not conflicting_bookings.exists()

# Create your views here 
from .models import Room, Booking
from .forms import BookingForm
from django import forms
from django.contrib.auth.decorators import login_required

# View для відображення всіх кімнат
def room_list_view(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

# View для створення бронювання (з використанням форми)
def booking_create_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Призначаємо користувача, який робить бронювання
            if booking.is_available():
                booking.save()
                return redirect('booking_success')
            else:
                form.add_error(None, "Вибрані дні не доступні.")
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})

# View для відображення успішного бронювання
def booking_success_view(request):
    return render(request, 'booking_success.html')


