from django.shortcuts import render, redirect
from home.models import *
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate
from login.forms import HandelPasswordForm


# Create your views here.


def dashboard(request):
    if request.user.is_authenticated:
        response_ = redirect('/dashboard/profile')
        return response_
    else:
        return redirect("/SS-admin")


def user_profile(request):
    if request.user.is_authenticated:
        about = About.objects.all()
        return render(request, 'dashboard/users-profile.html', {'about': about})
    else:
        return redirect("/SS-admin")


def userinfo_update(request):
    if request.user.is_authenticated:
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
    else:
        return redirect("/SS-admin")


def skills(request):
    about = About.objects.all()
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = Skill_form(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                redirect("/add-skills")
        else:
            fm = Skill_form()
        return render(request, 'dashboard/skills.html', {'about': about, 'form': fm})
    else:
        return redirect("/SS-admin")


def hero(request):
    about = About.objects.all()
    hero = Hero.objects.all()
    length_ = len(hero)
    if request.user.is_authenticated:
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
    else:
        return redirect("/SS-admin")


def update_hero(request):
    about = About.objects.all()
    hero = Hero.objects.all()
    length_ = len(hero)
    if request.user.is_authenticated:
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
    else:
        return redirect("/SS-admin")


def services_list(request):
    about = About.objects.all()
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = Services_form(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                return redirect("/dashboard/add-services-info")
        else:
            fm = Services_form()
        return render(request, 'dashboard/services.html', {'about': about, 'form': fm})
    else:
        return redirect("/SS-admin")


def portfolio_list(request):
    about = About.objects.all()
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = Portfolio_form(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                return redirect("/dashboard/add-portfolio-info")
        else:
            fm = Portfolio_form()
        return render(request, 'dashboard/portfolio_item.html', {'about': about, 'form': fm})
    else:
        return redirect("/SS-admin")


def blog_list(request):
    about = About.objects.all()
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = Blog_form(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                return redirect("/dashboard/add-blog-info")
        else:
            fm = Blog_form()
        return render(request, 'dashboard/blog_item.html', {'about': about, 'form': fm})
    else:
        return redirect("/SS-admin")


def testimonial(request):
    about = About.objects.all()
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = testimonial_form(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                return redirect("/dashboard/add-testimonial-info")
        else:
            fm = testimonial_form()
        return render(request, 'dashboard/testimonial.html', {'about': about, 'form': fm})
    else:
        return redirect("/SS-admin")


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
    if request.user.is_authenticated:
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
    else:
        return redirect("/SS-admin")


def table_view(request):
    if request.user.is_authenticated:
        skill = Skill.objects.all()
        about = About.objects.all()
        services = Services_list.objects.all()
        portfolio = Portfolio_item.objects.all()
        testimonial = Testimonial.objects.all()
        blog = Blog_item.objects.all()
        context = {
            'skills': skill,
            'about': about,
            'services': services,
            'portfolio': portfolio,
            'testimonial': testimonial,
            'blog': blog
        }
        return render(request, 'dashboard/tables.html', context)
    else:
        return redirect("/SS-admin")


def change_password(request):
    if request.user.is_authenticated:
        about = About.objects.all()
        if request.method == "POST":
            fm = HandelPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
        else:
            fm = HandelPasswordForm(user=request.user)
        return render(request, 'dashboard/change_password.html', {'form': fm, 'about': about})
    else:
        return redirect("/SS-admin")


def delete(request):
    data = request.POST
    id = data.get('id')
    skills = Skill.objects.get(id=id)
    skills.delete()
    return redirect('/dashboard/table-list')


# services delete
def delete_services(request):
    data = request.POST
    id = data.get('id')
    services = Services_list.objects.get(id=id)
    services.delete()
    return redirect('/dashboard/table-list')


# portfolio delete

def delete_portfolio(request):
    data = request.POST
    id = data.get('id')
    portfolio = Portfolio_item.objects.get(id=id)
    portfolio.delete()
    return redirect('/dashboard/table-list')

# testimonial delte


def delete_testimonial(request):
    data = request.POST
    id = data.get('id')
    testimonial = Testimonial.objects.get(id=id)
    testimonial.delete()
    return redirect('/dashboard/table-list')

# blog delet


def delete_blog(request):
    data = request.POST
    id = data.get('id')
    blog = Blog_item.objects.get(id=id)
    blog.delete()
    return redirect('/dashboard/table-list')
