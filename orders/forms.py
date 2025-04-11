# orders/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import User, Profile  # Import your custom user model and profile model


class CustomUserCreationForm(UserCreationForm):
    terms_and_conditions = forms.BooleanField(required=True, label="I agree to the terms and conditions")
    address = forms.CharField(max_length=255)
    mobile_number = forms.CharField(max_length=20, required=False, label="Mobile Number")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists. Please choose another one.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

def save(self, commit=True):
    user = super().save(commit=False)
    user.email = self.cleaned_data['email']  # Ensures email is saved
    if commit:
        user.save()

        # Check if profile already exists before creating a new one
        if not Profile.objects.filter(user=user).exists():
            Profile.objects.create(
                user=user,
                address=self.cleaned_data['address'],
                phone_number=self.cleaned_data.get('mobile_number')
            )
    return user



# Login Form
class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        required=True
    )


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone_number']
