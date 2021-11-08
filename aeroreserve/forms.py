from django import forms
from aeroreserve.models import Passenger, Ticket
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ('other', 'OTHER'),
)

class PassengerForm(forms.ModelForm):
    passenger_firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col textbox-translucent', 'autocomplete': 'off', 'placeholder': 'First Name'}), label='')
    passenger_lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col textbox-translucent', 'autocomplete': 'off', 'placeholder': 'Last Name'}), label='')
    passenger_dob = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control datepicker textbox-translucent', 'autocomplete': 'off', 'placeholder': 'Date of Birth'}), label='')
    passenger_gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(), label='')
    SSN = forms.CharField(max_length=12, min_length=12, widget=forms.TextInput(attrs={'class': 'form-control textbox-translucent', 'autocomplete': 'off', 'placeholder': 'Aadhaar Number'}), label='')
    class Meta():
        model = Passenger
        fields = (
            'passenger_firstname',
            'passenger_lastname',
            'passenger_dob',
            'passenger_gender',
            'SSN',
        )