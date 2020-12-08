from django.urls import path
from .views import MapView

app_name = 'world'
urlpatterns = [
    path('', MapView.as_view(), name='index'),
]
