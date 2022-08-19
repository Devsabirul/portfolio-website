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
            "Cover": forms.FileInput(attrs={'class': 'form-control mt-3 mb-3'}),
            "heading": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Heading'}),
            'cv': forms.FileInput(attrs={'class': 'form-control mt-3 mb-3'}),
            "t1": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Typing Effect 1st '}),
            "t2": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Typing Effect 2nd '}),
            "t3": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Typing Effect 3rd '}),
            "t4": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Typing Effect 4th '}),
        }


class Services_form(forms.ModelForm):
    class Meta:
        model = Services_list
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'service title'}),
            "description": forms.Textarea(attrs={'class': 'form-control mt-3', 'placeholder': 'service description'}),
            "icon": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'service icon class name'}),
        }


class Portfolio_form(forms.ModelForm):
    class Meta:
        model = Portfolio_item
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Portfolio title'}),
            "description": forms.Textarea(attrs={'class': 'form-control mt-3', 'placeholder': 'portfolio description'}),
            "category": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'portfolio Category '}),
            "project_client": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'portfolio project_client'}),
            "url": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'portfolio url '}),
            'Picture': forms.FileInput(attrs={'class': 'form-control mt-3'}),
            'slider_one': forms.FileInput(attrs={'class': 'form-control mt-3'}),
            'slider_two': forms.FileInput(attrs={'class': 'form-control mt-3'}),
            'slider_three': forms.FileInput(attrs={'class': 'form-control mt-3'}),
        }


class Blog_form(forms.ModelForm):
    class Meta:
        model = Blog_item
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Blog title'}),
            "description": forms.Textarea(attrs={'class': 'form-control mt-3', 'placeholder': 'Blog description'}),
            "category": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Blog Category '}),
            "author": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Blog Author '}),
            'Picture': forms.FileInput(attrs={'class': 'form-control mt-3'}),
        }


class testimonial_form(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = "__all__"
        widgets = {
            "description": forms.Textarea(attrs={'class': 'form-control mt-3', 'placeholder': 'Testimonial description'}),
            "author": forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Testimonial Author '}),
            'photo': forms.FileInput(attrs={'class': 'form-control mt-3'}),
        }
