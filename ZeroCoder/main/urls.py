from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new/', views.new, name='new'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
]