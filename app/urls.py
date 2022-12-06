from django.urls import path,include
from .views import linwilson
urlpatterns = [
    path('', linwilson),
]