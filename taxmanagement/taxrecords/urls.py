from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.create_view, name='create'),
    path('read/', views.read_view, name='read'),
    path('update/<int:pk>/', views.update_view, name='update'),
    path('delete/<int:pk>/', views.delete_view, name='delete'),
    path('bulk_import/', views.bulk_import_view, name='bulk_import'),
]