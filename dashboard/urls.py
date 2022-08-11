from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('profile', user_profile, name="user_profile"),
    path('update', userinfo_update, name="userinfo_update"),
    path('add-skills', skills, name="skills"),
    path('add-cover-info', hero, name="hero"),
    path('update-hero', update_hero, name="update_hero"),
    path('add-services-info', services_list, name="services_list"),
    path('add-portfolio-info', portfolio_list, name="portfolio_list"),
    path('add-blog-info', blog_list, name="blog_list"),
    path('add-testimonial-info', testimonial, name="testimonial"),
    path('others-component', otherComponent, name="otherComponent"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
