from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.db import models


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    address = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=20, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            profile = self.instance.profile
            self.fields['address'].initial = profile.address
            self.fields['phone_number'].initial = profile.phone_number
        except Profile.DoesNotExist:
            pass

    def save(self, commit=True):
        user = super().save(commit=commit)
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            profile = Profile(user=user)
        profile.address = self.cleaned_data['address']
        profile.phone_number = self.cleaned_data['phone_number']
        if commit:
            profile.save()
        return user