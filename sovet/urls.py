from django.urls import path
from .views import *

urlpatterns = [
    path('', board_of_trustees.as_view(), name='board_of_trustees'),
    path('<str:slug>/', get_one_board_of_trustees.as_view(), name='get_one_board_of_trustees'),

]

