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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
