from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('create/', views.doctor_create, name='doctor_create'),
    path('update/<int:id>/', views.doctor_update, name='doctor_update'),
    path('delete/<int:id>/', views.doctor_delete, name='doctor_delete'),
]