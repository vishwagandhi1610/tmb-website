from ast import Break
from atexit import register
from http.cookiejar import FileCookieJar
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from home.models import Contact
from django.views.decorators.csrf import csrf_exempt
from itertools import chain
import json
from django import template
from .models import *


register = template.Library()

pe = []
li = []

import logging
logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    context = {
        "variable":"this is sent"
    }
    return render(request, 'index.html',context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('this is about page')    

def services(request):
    return render(request, 'services.html')
    #return HttpResponse('this is service page')

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse('this is contact page')

def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()

    return render(request, 'contact.html')
    #return HttpResponse('this is add endpoint')

@csrf_exempt
def webhook(request):
    req = json.loads(request.body.decode("utf-8"))
    action = req.get('queryResult').get('action')
    logger.warning('We have the action')
    global pe
    global li
    if action == 'get_menu':
        logger.warning("Inside the if loop......")
        fulfillmentText = {'fulfillmentText':'menu will be served.'}
        return JsonResponse(fulfillmentText , safe= False)

    elif action == 'get_flavour' or action == 'get_type':
       
        logger.warning("It is here")
        data = req.get('queryResult').get('parameters')
        logger.warning("-----------------%s",data)

        param = list(data.keys())
        paramtwo = list(data.values())
        li.append(paramtwo)
        
        logger.warning('print.......%s',param)
        pe.append(param)
        logger.warning("list.......%s",pe)

        if len(pe) == 1:

            if param[0] == 'flavours':
                logger.warning("Insisdddeeeeeee")
                fulfillmentText = {'fulfillmentText':'Can you tell which type do you want?'}
                return JsonResponse(fulfillmentText , safe= False)
                       
            elif param[0] == 'icetype':
                fulfillmentText = {'fulfillmentText':'yeah sure, Can you tell which type of flavour do you want?'}
                return JsonResponse(fulfillmentText, safe=False)

        if len(pe) == 2:
            logger.warning("You have both the parameters.....")
            logger.warning(".........values of dict..........%s",li)
            for val in li:
                logger.warning(",,,,,,,,,,,,%s",val)
                if type.objects.filter(name=val[0]).exists():
                    data = type.objects.get(name=val[0])
                    aval = data.avail
                    if aval == "yes":
                        logger.warning('I am in yes...........')
                        if flavour.objects.filter(name=val[1]).exists():
                            logger.warning("I got the flavourrrrrr")
                            fla = flavour.objects.get(name = val[1])
                            ava = fla.avail
                            if ava == "yes":
                                logger.warning("I am in yesssssssssssss")
                                fulfillmentText = {'fulfillmentText':'Yes it is available'}
                                return JsonResponse(fulfillmentText, safe= False)

                            elif ava == "no":
                                logger.warning("I am in nooooooooo")
                                fulfillmentText = {'fulfillmentText':'No it is not available'}
                                return JsonResponse(fulfillmentText, safe= False)

                        else:
                            fulfillmentText = {'fulfillmentText':'SORRY WE DO NOT HAVE THAT SUPPLY'}
                            return JsonResponse(fulfillmentText, safe= False)



                    elif aval == "no":
                        fulfillmentText = {'fulfillmentText':'No it is not available'}
                        return JsonResponse(fulfillmentText, safe= False)

                else:
                    logger.warning("You are in the else blockkkkkkkkk")

                






                    

            
            

            

            

            

       


        



 
            
            

    

    

    

    

    

        

