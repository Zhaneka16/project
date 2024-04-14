from django.shortcuts import render
from django.http import HttpResponse
from main.models import Design_object, Spot

def design_object(request): 
    objs = Design_object.objects.all()
    spots = Spot.objects.all()
    data = {'titles':'All objects',
    'objs': objs,
    'spots': spots, }
    return render(request, 'main.html', context=data)


# def spot(request): 
#     spots = Spot.objects.all()
#     data = {'spots': spots, }
#     return render(request, 'main.html', context=data)



def index(request):
    # print(request)
    # print(request.scheme)   
    # print(request.path)
    # print(request.encoding) 
    return HttpResponse('<h1>Hello word!</h1>')

def about(request):
    return HttpResponse('<a href="#"> About page!</a>')

def contacts(request):
    return HttpResponse('<h2>Contacts</h2>')  

def ggg(request):
    return HttpResponse('<h1>Повтор</h1>')

def numbers(request):
    return HttpResponse('<h2>numbers</h2>') 

def arhive(request):
    return HttpResponse('<h2>arhive</h2>') 

def vse_proyekty(request):
    return HttpResponse('<p>АРХИТЕКТУРА</p>')
