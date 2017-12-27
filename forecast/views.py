# -*- coding: utf-8 -*-



from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse 

#from .forms import DocumentForm
#from .forms import ArimaForm
#from  .forms import CrostonForm

#from .models import Document
#from .models import Arima
#from .models import Croston 

from .models import *
from .forms import *


from django.contrib.staticfiles.templatetags.staticfiles import static
from holtwinter import mainfn
from croston import croston
from fb import fbprophet
from decompose import decompose

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import subprocess




# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the  site index page")


def model_form_upload(request): ### for holtwinter 
    para = False
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = Document.objects.all()[len(Document.objects.all())-1]
            mainfn(obj.seasonal_length , obj.forecast_period, obj.holt_w, "/home/pramod/Desktop/analytics/"+obj.document.name )
            para = True
    else:
        form = DocumentForm()
    return render(request, 'forecast/model_form_upload.html',  {
        'form': form, 'para': para,
    })

def crostonview(request):
    para= False
    if request.method=='POST':
        
        form=CrostonForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            obj=Croston.objects.all()[len(Croston.objects.all())-1]
        ####  call the python script
            croston(obj.document.name)
            para =True
    else : 
        form =CrostonForm()
    return render(request, 'forecast/croston.html',  {
        'form': form, 'para': para,
    })
    
    

def arimaview(request):
    ### do something here ##
    para= False
    if request.method=='POST':
        form=ArimaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            obj=Arima.objects.all()[len(Arima.objects.all())-1]
        ####  call the python script  after this line
            para =True
    else : 
        form =ArimaForm()
    return render(request, 'forecast/arima.html',  {
        'form': form, 'para': para,
    })
    

def fbprophetview(request):
    ### do something here ##
    para= False
    if request.method=='POST':
        form=FbprophetForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            obj=Fbprophet.objects.all()[len(Fbprophet.objects.all())-1]
            fbprophet(obj.document.name)
            para =True
    else : 
        form =FbprophetForm()
    return render(request, 'forecast/fbprophet.html',  {
        'form': form, 'para': para,
    })




def decompositionview(request):
    ### do something here ##
    para= False
    if request.method=='POST':
        form=DecompositionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            obj=Decomposition.objects.all()[len(Decomposition.objects.all())-1]
            decompose(obj.document.name)
            para =True
    else : 
        form =DecompositionForm()
    return render(request, 'forecast/decomposition.html',  {
        'form': form, 'para': para,
    })
