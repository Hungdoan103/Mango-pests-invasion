from django.urls import path
from . import views

urlpatterns = [
    path('', views.history_list, name='history_list'),
    path('record/<int:session_id>/', views.record_result, name='record_result'),
    path('detail/<int:history_id>/', views.history_detail, name='history_detail'),
    path('list/', views.history_list, name='history_list'),
]
