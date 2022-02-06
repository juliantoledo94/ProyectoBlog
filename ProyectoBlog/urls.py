from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("loginApp.urls")),
    path('registerLoginApp/',include('django.contrib.auth.urls')),
    path('registerLoginApp/', include('registerLoginApp.urls')),
    path('perfilesApp/',include('django.contrib.auth.urls')),
    path('perfilesApp/',include('perfilesApp.urls')),
    path('mensajeriaApp/',include('django.contrib.auth.urls')),
    path('mesajeriaApp/',include('mensajeriaApp.urls')),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)