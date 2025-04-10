from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('details/<int:item_id>/', views.project_detail, name='project_detail'),
    path('about/', views.about, name='about'),
]
