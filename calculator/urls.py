from django.urls import path
from mysimplecalulator import views

urlpatterns = [
        path('thiyagu/mysimplecalulator/app', views.calculator, name='calculator'),
]
