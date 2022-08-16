from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
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
    path('table-list', table_view, name="table_view"),
    path('change_password', change_password, name="change_password"),
    path('delete', delete, name="delete"),
    path('delete_services', delete_services, name="delete_services"),
    path('delete_portfolio', delete_portfolio, name="delete_portfolio"),
    path('delete_testimonial', delete_testimonial, name="delete_testimonial"),
    path('delete_blog', delete_blog, name="delete_blog"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
