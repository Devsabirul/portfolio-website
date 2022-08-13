from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from login.views import user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('SS-admin', include('login.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('logout', user_logout, name="user_logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
