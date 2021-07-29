from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='glavnaya'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('news/<str:slug>/', GetPost.as_view(), name='post'),
    path('post-comments/', base_view),
    path('create-comments/', create_comment, name='comment_create'),
    path('comment-complain/', complain, name='comment_complain'),
    path('create-child-comment/', create_child_comment, name='comment_child_create'),

    path('listnews', views.listnews, name='listnews'),



    path('addnews', views.addnews, name='addnews'),
    path('addnewscategory', views.addnewscategory, name='addnewscategory'),
    path('addnewstag', views.addnewstag, name='addnewstag'),

]

