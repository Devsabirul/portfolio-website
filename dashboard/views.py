from http.client import HTTPResponse
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
    if request.method == "POST":
        fm = Skill_form(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            redirect("/add-skills")
    else:
        fm = Skill_form()
    return render(request, 'dashboard/skills.html', {'about': about, 'form': fm})


def hero(request):
    about = About.objects.all()
    hero = Hero.objects.all()
    length_ = len(hero)
    if length_ == 0:
        if request.method == "POST":
            fm = Hero_form(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                return redirect('/dashboard/')
        else:
            fm = Hero_form()
        return render(request, 'dashboard/hero.html', {'about': about, 'form': fm, 'hero': hero})
    else:
        return redirect('/dashboard/update-hero')


def update_hero(request):
    about = About.objects.all()
    hero = Hero.objects.all()
    length_ = len(hero)
    if length_ == 0:
        return redirect('/dashboard/add-cover-info')
    else:
        if request.method == "POST":
            get_id = Hero.objects.get(id=1)
            fm = Hero_form(request.POST, request.FILES, instance=get_id)
            if fm.is_valid():
                fm.save()
        else:
            get_id = Hero.objects.get(id=1)
            fm = Hero_form(instance=get_id)
        return render(request, 'dashboard/hero_update.html', {'form': fm, 'hero': hero, 'about': about})


def services_list(request):
    about = About.objects.all()
    if request.method == "POST":
        fm = Services_form(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect("/dashboard/add-services-info")
    else:
        fm = Services_form()
    return render(request, 'dashboard/services.html', {'about': about, 'form': fm})


def portfolio_list(request):
    about = About.objects.all()
    if request.method == "POST":
        fm = Portfolio_form(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect("/dashboard/add-portfolio-info")
    else:
        fm = Portfolio_form()
    return render(request, 'dashboard/portfolio_item.html', {'about': about, 'form': fm})


def blog_list(request):
    about = About.objects.all()
    if request.method == "POST":
        fm = Blog_form(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect("/dashboard/add-blog-info")
    else:
        fm = Blog_form()
    return render(request, 'dashboard/blog_item.html', {'about': about, 'form': fm})


def testimonial(request):
    about = About.objects.all()
    if request.method == "POST":
        fm = testimonial_form(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect("/dashboard/add-testimonial-info")
    else:
        fm = testimonial_form()
    return render(request, 'dashboard/testimonial.html', {'about': about, 'form': fm})


def otherComponent(request):
    about = About.objects.all()
    services = Services.objects.all()
    blog = Blog.objects.all()
    portfolio = Portfolio.objects.all()
    count = Count.objects.all()
    context = {
        'services': services,
        'about': about,
        'blog': blog,
        'portfolio': portfolio,
        'count': count
    }
    if request.method == "POST":
        services = Services(id=1)
        services.description = request.POST['services']
        services.save()
        blog = Blog(id=1)
        blog.description = request.POST['blog']
        blog.save()
        portfolio = Portfolio(id=1)
        portfolio.description = request.POST['portfolio']
        portfolio.save()
        count = Count(id=1)
        count.work = request.POST['work']
        count.experience = request.POST['experience']
        count.total_client = request.POST['client']
        count.award_won = request.POST['award_won']
        count.save()

    return render(request, 'dashboard/otherComponent.html', context)


