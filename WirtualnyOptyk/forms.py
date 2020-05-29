from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email,ValidationError
from WirtualnyOptyk.models import Supply, Profile, Order


class SearchForm(forms.Form):
    name=forms.CharField(max_length=50, required=False)


class CreateProfileForm(forms.ModelForm):
    password2=forms.CharField(max_length=30,widget=forms.PasswordInput)
    phone_number=forms.CharField(max_length=30)
    adress=forms.CharField(max_length=100)

    class Meta:
        model=User
        help_texts={"username":""}
        fields=('username','password','password2', 'first_name', 'last_name', 'email',"adress")
        widgets={
            "password":forms.PasswordInput,
            "email":forms.EmailInput
        }
        validators={
            "email":validate_email
        }

    def clean(self):
        super().clean()
        if self.cleaned_data["password2"]!=self.cleaned_data["password"]:
            raise ValidationError ("Password need to match")

class Supply_Form(forms.ModelForm):
    class Meta:
        model=Order
        fields=["provider"]









