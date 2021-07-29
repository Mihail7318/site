from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listtaski'),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('addtaski', views.addtaski, name='addtaski'),

]