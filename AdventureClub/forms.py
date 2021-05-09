from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import AdventureClub, AdventureEvent


class clubRegisterationForm(forms.ModelForm):
    owner = forms.CharField.widget(attrs={'readonly': 'true'})

    class Meta:
        model = AdventureClub
        fields = '__all__'
        exclude = ('owner', 'featured',)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class DateInput(forms.DateInput):
    input_type = 'date'


class adventureEventform(forms.ModelForm):
    class Meta:
        model = AdventureEvent
        exclude = ('event_by','featured',)
        fields = '__all__'
        widgets = {
            'event_start_date': DateInput(),
            'event_end_date': DateInput(),
        }
