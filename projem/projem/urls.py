from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
 path('', views.anasayfa, name="anasayfa"),
 path('urunler/', include('urunler.urls')),
 path('admin/', admin.site.urls),
 path('login', views.user_login),
 path('register', views.user_register),
 path('logout', views.user_logout),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
