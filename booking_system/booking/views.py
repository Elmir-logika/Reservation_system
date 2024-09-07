from django.shortcuts import render, redirect

# Create your views here 
from .models import Room, Booking
from .forms import BookingForm

# View для відображення всіх кімнат
def room_list_view(request):
    rooms = Room.objects.all()
    return render(request, 'booking/room_list.html', {'rooms': rooms})

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
                form.add_error(None, "Selected dates are not available.")
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form})

# View для відображення успішного бронювання
def booking_success_view(request):
    return render(request, 'booking/booking_success.html')


