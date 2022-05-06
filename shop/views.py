 
from tkinter import E
from unicodedata import category
from django.shortcuts import get_object_or_404, render
from shop.models import *
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator,InvalidPage,EmptyPage

# Create your views here.

def home(request,c_slug=None):
    c_page=None
    prods=None
    if c_slug != None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prods=products.objects.all().filter(category=c_page,avbl=True)
    else:
        prods=products.objects.all().filter(avbl=True)
    ct=categ.objects.all()
    p=Paginator(prods,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=p.page(page)
    except(InvalidPage,EmptyPage):
        pro=Paginator.page(Paginator.num_pages)
    return render(request,'home.html',{'prods':prods,'ct':ct,'pg':pro})

def proddetails(request,c_slug,prod_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=prod_slug)
    except Exception as e:
       raise e

    return render(request,'item.html',{'pr':prod})

def searching(request):
    prod=None
    query=None
    if 'q' in  request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'qr':query,'pr':prod})

    