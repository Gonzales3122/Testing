from django.shortcuts import render
from .forms import ReservationForm
from .models import ReservationModel
from . import views

def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Create a new ReservationModel instance and save the form data
            reservation = ReservationModel(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                date=form.cleaned_data['date'],
                arrival_time=form.cleaned_data['arrival_time'],
                vehicle_type=form.cleaned_data['vehicle_type'],
            )
            reservation.save()

            # Redirect to a success page or render a confirmation message
            return render(request, 'Page/success.html', {'name': reservation.name})
    else:
        form = ReservationForm()

    return render(request, 'Page/reservation.html', {'form': form})

def index(request):
    return render(request, template_name='Page/home.html')

def about(request):
    return render(request, template_name='Page/about.html')

def contact(request):
    return render(request, template_name='Page/contact.html')

def services(request):
    return render(request, template_name='Page/services.html')   

def reservation(request):
    return render(request, template_name='Page/reservation.html')

def success(request):
    return render(request, template_name='Page/success.html')

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import ReservationModel
from .forms import ReservationForm

def reservation_list(request):
    reservations = ReservationModel.objects.all()
    return render(request, 'Page/reservation_list.html', {'reservations': reservations})

def reservation_detail(request, pk):
    reservation = get_object_or_404(ReservationModel, pk=pk)
    return render(request, 'Page/reservation_detail.html', {'reservation': reservation})

def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()

    return render(request, 'Page/reservation_form.html', {'form': form})

def reservation_update(request, pk):
    reservation = get_object_or_404(ReservationModel, pk=pk)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'Page/reservation_form.html', {'form': form})

def reservation_delete(request, pk):
    reservation = get_object_or_404(ReservationModel, pk=pk)
    reservation.delete()
    return redirect('reservation_list')
