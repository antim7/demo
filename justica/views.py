
from django.shortcuts import render, get_object_or_404, redirect


from django.http import JsonResponse

from django.conf import settings


# Create your views here.
def home(request):
    context={}
    return render(request, 'justica/index.html',context)
    
def all_news(request):
    
    return render(request, 'justica/allnews.html')

def about(request):
    
    return render(request, 'justica/about.html')   
def contactinfo(request):
    
    return render(request, 'justica/contact.html')       

def practice_info(request):
    
    return render(request, 'justica/practiceArea.html')     