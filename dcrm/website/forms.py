from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class RecordForm(forms.ModelForm):
            first_name = forms.CharField(required=True)
            last_name = forms.CharField(required=True)
            email = forms.EmailField(required=True)
            phone = forms.CharField(required=True)
            address = forms.CharField(required=True)
            city = forms.CharField(required=True)
            class Meta:
                model = Customer
                exclude = ("user",)
                fields = '__all__'
                widgets = {'created_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),}
                
                