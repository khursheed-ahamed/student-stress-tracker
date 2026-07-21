from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DailyInput

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DailyInputForm(forms.ModelForm):
    class Meta:
        model = DailyInput
        fields = ['mood', 'sleep_duration', 'workload', 'notes']
        widgets = {
            'mood': forms.Select(attrs={'class': 'form-control'}),
            'sleep_duration': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.5'}),
            'workload': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '10'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }