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
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(required=True, label="First Name")
    last_name = forms.CharField(required=True, label="Last Name")
    mobile_number = forms.CharField(required=False, label="Mobile Number")
    address = forms.CharField(widget=forms.Textarea, required=False, label="Address")

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name",
                  "password1", "password2", "mobile_number", "address")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
            profile = user.profile
            profile.mobile_number = self.cleaned_data['mobile_number']
            profile.address = self.cleaned_data['address']
            profile.save()
        return user

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    address = forms.CharField(max_length=255, required=False)
    mobile_number = forms.CharField(max_length=20, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            profile = self.instance.profile
            self.fields['address'].initial = profile.address
            self.fields['mobile_number'].initial = profile.mobile_number
        except Profile.DoesNotExist:
            pass

    def save(self, commit=True):
        user = super().save(commit=commit)
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            profile = Profile(user=user)
        profile.address = self.cleaned_data['address']
        profile.mobile_number = self.cleaned_data['mobile_number']
        if commit:
            profile.save()
        return user