# your_app/forms.py
from django import forms

class ReservationForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    
    # Choices for the date field
    date_choices = [
        ('2024-02-03', '2024-02-03'),
        ('2024-02-04', '2024-02-04'),
        # Add more choices as needed
    ]
    date = forms.ChoiceField(label='Reservation Date (YEAR-M-D)', choices=date_choices)

    # Choices for the arrival_time field
    arrival_time_choices = [
        ('08:00', '8:00 AM'),
        ('12:00', '12:00 PM'),
        # Add more choices as needed
    ]
    arrival_time = forms.ChoiceField(label='Arrival Time (H:M)', choices=arrival_time_choices)

    vehicle_type = forms.CharField(label='Vehicle Type', max_length=50)

# forms.py
from django import forms
from .models import ReservationModel

class ReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationModel
        fields = '__all__'
