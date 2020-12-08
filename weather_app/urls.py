"""weather_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.gis import admin
from django.urls import include, path
from django.views.generic import TemplateView

from weather_app.views import SignUpView
from world import views
from .views import AccountView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', include('world.urls')),
    path('myaccount/', AccountView.as_view(), name='account'),
    path('getweather/', views.get_weather, name='getweather'),
    path('reversegeocode/', views.reverse_geocode, name='reversegeocode'),
    path('addlocation/', views.create_previous_location, name='addlocation'),
    path('getlocations/', views.get_previous_locations, name='getlocations'),
    path('forwardgeocode/', views.forward_geocode, name='forwardgeocode'),
    path('offline/', TemplateView.as_view(template_name='offline.html'), name='offline'),
    path('', include('pwa.urls')),
]
