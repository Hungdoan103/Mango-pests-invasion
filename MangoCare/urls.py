"""
URL configuration for MangoCare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('pest-disease/', include('pest_disease.urls')),
    path('pest-disease-detail/', include('pest_disease_detail.urls')),
    path('about-us/', include('about_us.urls')),
    path('pests/', RedirectView.as_view(url='/pest-disease/', permanent=True)),
    path('project1/', include('app_project1.urls')),
    
    # URL patterns cho các app mới
    path('auth/', include('user_auth.urls')),
    path('surveillance/', include('surveillance.urls')),
    path('surveillance-history/', include('surveillance_history.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
