from xml.dom.minidom import Document
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', home, name="home"),
    path('portfolio/<slug:slug>', portfolio_single_page,
         name="portfolio_single_page"),
    path('blog/<slug:slug>', blog_single_page, name="blog_single_page")
]
