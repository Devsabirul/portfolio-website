from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    about = About.objects.all()
    hero = Hero.objects.all()
    skill = Skill.objects.all()
    services = Services.objects.all()
    services_list = Services_list.objects.all()
    portfolio = Portfolio.objects.all()
    portfolio_list = Portfolio_item.objects.all()
    blog = Blog.objects.all()
    blog_list = Blog_item.objects.all()
    count = Count.objects.all()
    testimonial = Testimonial.objects.all()
    # sliceing
    blog_slice_title = []
    blog_slice_description = []
    context = {
        'about': about,
        'hero': hero,
        'skill': skill,
        'services': services,
        'services_list': services_list,
        'portfolio': portfolio,
        'portfolio_list': portfolio_list,
        'blog': blog,
        'blog_title': blog_slice_title,
        'blog_description': blog_slice_description,
        'blog_list': blog_list,
        'count': count,
        'testimonial': testimonial
    }
    for i in blog_list:
        blog_slice_title.append(i.title[0:29])
        blog_slice_description.append(i.description[0:140])

    print(blog_slice_title)
    return render(request, 'home/index.html', context)


def portfolio_single_page(request, slug):
    about = About.objects.all()
    portfolio = Portfolio_item.objects.get(slug=slug)
    return render(request, 'singlepage/portfolio-details.html', {'portfolio': portfolio, 'about': about})


def blog_single_page(request, slug):
    about = About.objects.all()
    blog = Blog_item.objects.get(slug=slug)
    return render(request, 'singlepage/blog-single.html', {'blog': blog, 'about': about})
