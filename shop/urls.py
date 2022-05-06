from unicodedata import name
from django.urls import path
from . import views
from .views import *


urlpatterns=[
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<slug:c_slug>/<slug:prod_slug>',views.proddetails,name='detail'),
    path('search',views.searching,name='search')
]