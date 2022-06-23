from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import SEND_DATA
from django.utils import timezone
# Create your views here.

# 메인화면 데이터 전송
def Home(request) :

    if request.method == "POST":
        
        # 입력 값 받아오기
        temp = request.POST.get('keyword_input')
        start = request.POST.get('start')
        end = request.POST.get('end')

        # 입력 값 전달 
        keyword = SEND_DATA()

        keyword.text = temp
        keyword.start_day = start
        keyword.end_day = end
        
        # 입력 값 확인
        #print('-'*20)
        #print(keyword.start_day)
        #print(keyword.end_day)
        #print('-'*20)

        # DB에 저장
        keyword.save()
        
        keyword_list = SEND_DATA.objects.all()
        return render(request, 'DH_service/home.html', context={'keyword_list': keyword_list})
       
    else:
        keyword_list = SEND_DATA.objects.all()
        return render(request, 'DH_service/home.html', context={'keyword_list': keyword_list})
