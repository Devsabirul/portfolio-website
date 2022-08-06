from django.shortcuts import render, redirect
from home.models import *
from .form import *


# Create your views here.


def dashboard(request):
    response_ = redirect('/dashboard/profile')
    return response_


def user_profile(request):
    about = About.objects.all()
    return render(request, 'dashboard/users-profile.html', {'about': about})


def userinfo_update(request):
    if request.method == "POST":
        about = About(id=1)
        about.name = request.POST['name']
        about.about_me = request.POST['about']
        about.profile = request.POST['profile']
        about.location = request.POST['location']
        about.phone = request.POST['phone']
        about.email = request.POST['email']
        about.facebook = request.POST['facebook']
        about.instagram = request.POST['instagram']
        about.linkedin = request.POST['linkedin']
        if len(request.FILES) != 0:
            about.photo = request.FILES['profile_pic']
            about.logo = request.FILES['logo']
        about.save()
    response = redirect('/dashboard/profile')
    return response


def skills(request):
    about = About.objects.all()
    fm = Skill_form()
    return render(request, 'dashboard/skills.html', {'about': about, 'form': fm})
