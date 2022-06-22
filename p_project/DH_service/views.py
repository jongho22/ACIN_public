from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import SEND_DATA
# Create your views here.

# 메인화면 
def Home(request) :

    if request.method == "POST":
        
        temp = request.POST.get('keyword_input')

        keyword = SEND_DATA()
    
        keyword.text = temp
        
        keyword.save()
        
        keyword_list = SEND_DATA.objects.all()
        return render(request, 'DH_service/home.html', context={'keyword_list': keyword_list})
       
    else:
        keyword_list = SEND_DATA.objects.all()
        return render(request, 'DH_service/home.html', context={'keyword_list': keyword_list})
