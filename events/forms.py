from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Event, Discipline

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['illustration', 'title', 'discipline', 'date', 'time', 'max_participants', 'description', 'illustration']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    discipline = forms.ModelChoiceField(
        queryset=Discipline.objects.all(),  # Récupérer toutes les disciplines
        empty_label="Choisissez une discipline",  # Option par défaut dans le menu déroulant
    )

from django import forms
from .models import User, Event

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'profile_picture']



        





