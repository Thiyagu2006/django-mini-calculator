from django.contrib import admin
from django.urls import path
from mysimplecalulator import views

urlpatterns = [
    path('', views.calculator, name='home'),  # default home page
    path('admin/', admin.site.urls),
    path('thiyagu/mysimplecalulator/app', views.calculator, name='calculator'),
]
