from django.shortcuts import get_object_or_404, redirect, render
from mysqlx import DocResult
from shop.models import *
from .models import *
# Create your views here.
def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id



def cartdetails(request,tot=0,count=0,ct_items=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.all().filter(cart=ct,active=True)
        for i in ct_items:
            tot=tot+(i.prodt.price)*(i.qty)
            count=count+(i.qty)
    except cartlist.DoesNotExist:
        pass
    return render(request,'cart.html',{'t':tot,'cnt':count,'ci':ct_items})

def addcart(request,product_id):
    prod=products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(cart=ct,prodt=prod)
        if c_items.prodt.stk > c_items.qty:
            c_items.qty += 1
            c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(cart=ct,prodt=prod,qty=1)
        c_items.save()
    return redirect('cartdetails')

def mincart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(cart=ct,prodt=prod)
    if c_items.qty > 1:
        c_items.qty -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartdetails')

def removecart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(cart=ct,prodt=prod)
    c_items.delete()
    return redirect('cartdetails')