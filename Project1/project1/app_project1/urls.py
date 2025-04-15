from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^projects/$', views.project_list, name='project_list'),
    re_path(r'^details/(?P<item_id>[DdPp][0-9]+)/$', views.project_detail, name='project_detail'),
    re_path(r'^about/$', views.about, name='about'),
]
