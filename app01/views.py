from django.shortcuts import render

# Create your views here.
from django.shortcuts import  render, HttpResponse

def index(request):
    return  HttpResponse('欢迎使用')



def user_list(request):

    #去app目录下的templates 目录下寻找user_list.html
    return render(request, "user_list.html")



def user_add(request):
    return render(request, "user_add.html")