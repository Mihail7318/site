from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *

urlpatterns = [
    #path('setting/', Setting),
    path('partner/', partner),
    path('', views.head),

    path('document/', document),
    path('faq/', faq),
    path('privacypolicy/', privacypolicy),
    path('contacts/', contact),
    path('aboutus/', aboutus),
    path('useragreement/', useragreement),

]
