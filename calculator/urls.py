from django.urls import path
from calculator import views

urlpatterns = [
        path('thiyagu/mysimplecalulator/app', views.calculator, name='calculator'),
]
