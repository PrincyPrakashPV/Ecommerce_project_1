from audioop import reverse
from operator import mod
from tabnanny import verbose
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from unicodedata import name
# Create your models here.
class categ(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    
    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('prod_cat',args=[self.slug,])

class products(models.Model):
    name=models.CharField(max_length=300,unique=True)
    slug=models.SlugField(max_length=300,unique=True)
    img=models.ImageField(upload_to='pic')
    price=models.FloatField()
    stk=models.IntegerField()
    desc=models.TextField()
    avbl=models.BooleanField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('detail',args=[self.category.slug,self.slug])
