from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('create', views.Create, name='Create'),
    path('update/<int:no>', views.Update, name='Update'),
    path('delete/<int:no>', views.Delete, name='Delete'),
]