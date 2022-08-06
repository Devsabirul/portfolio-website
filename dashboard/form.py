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
            "skill": forms.TextInput(attrs={'class': 'form-control mt-3'}),
            "percentage": forms.NumberInput(attrs={'class': 'form-control mt-3'})
        }
