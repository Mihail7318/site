from django.urls import path
from .views import *

urlpatterns = [
    path('', Homesmena.as_view(), name='glavnaya'),
    path('<str:slug>/', GetPostsmena.as_view(), name='postsmena'),


    #path('category/<str:slug>/', get_category, name='category'),
    #path('news/<int:news_id>/', view_news, name='view_news'),

]

