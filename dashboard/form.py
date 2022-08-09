from dataclasses import field
from django import forms
from home.models import *


class About_form(forms.ModelForm):
    class Meta:
        model = About
        fields = ['photo', 'logo']


class Skill_form(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        widgets = {
            "skill": forms.TextInput(attrs={'class': 'form-control mt-3 mb-3', 'placeholder': 'Enter your Skills type'}),
            "percentage": forms.NumberInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Enter your Skills Percentage'})
        }


class Hero_form(forms.ModelForm):
    class Meta:
        model = Hero
        fields = "__all__"
        widgets = {
            "img": forms.FileInput(attrs={'class': 'form-control mt-3 mb-3'}),
            "heading": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Enter your Skills Percentage'}),
            "t1": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Typing Effect 1st '}),
            "t2": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Typing Effect 2nd '}),
            "t3": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Typing Effect 3rd '}),
            "t4": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Typing Effect 4th '}),
        }
