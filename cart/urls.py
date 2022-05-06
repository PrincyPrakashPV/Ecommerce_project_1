import imp
from django.urls import path
from . import views

urlpatterns=[
    path('cartdetails',views.cartdetails,name='cartdetails'),
    path('addcart/<int:product_id>',views.addcart,name='addcart'),
    path('mincart/<int:product_id>',views.mincart,name='mincart'),
    path('removecart/<int:product_id>',views.removecart,name='removecart')
]