#imports for forms.py 
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This e-mail address is already in use. Please log in or reset your password.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'cheese', 'toppings']
        widgets = {
            'size': forms.Select(attrs={'class': 'form-control'}),
            'crust': forms.Select(attrs={'class': 'form-control'}),
            'sauce': forms.Select(attrs={'class': 'form-control'}),
            'cheese': forms.Select(attrs={'class': 'form-control'}),
            'toppings': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['toppings'].queryset = Topping.objects.all()
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-control'

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['name', 'address_line_1', 'address_line_2', 'city', 'county', 'eircode', 'card_number', 'cvv', 'expiry_date']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address_line_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 1'}),
            'address_line_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 2 (optional)'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'county': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'County (optional)'}),
            'eircode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eircode (optional)'}),
            'card_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Credit Card Number'}),
            'cvv': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVV'}),
            'expiry_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/YY'}),
        }