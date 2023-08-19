from django.urls import path
from . import views

urlpatterns = [
    path('', views.hof_page, name='hof'),
]