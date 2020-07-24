from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_list, name='cv_list'),
    path('cv_edit/', views.cv_edit, name='cv_edit'),
]