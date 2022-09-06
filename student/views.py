from datetime import datetime, timedelta
from email.policy import default
from unicodedata import name
from django.shortcuts import render

def setcookie(request):
    rpns = render(request, 'student/setcookie.html')
    rpns.set_cookie('name', 'Jasmine', max_age=60)
    return rpns

def setsignedcookie(request):
    rspns = render(request, 'student/setsigned.html')
    rspns.set_signed_cookie('name','Dhushi', salt='nm', max_age=60)
    return rspns

def getsignedcookie(request):
    name = request.get_signed_cookie('name', default='Guest', salt='nm')
    print(name)
    return render(request, 'student/getsigned.html')


def getcookie(request):
#    name = request.COOKIES['name'] #firt method
    # name = request.COOKIES.get('name' ) # 2 method
    name = request.COOKIES.get('name', 'Guest' ) # 3 method if no key is present
    return render(request, 'student/getcookie.html', {'name': name})

def delcookie(request):
    rpns = render(request, 'student/delcookie.html')
    rpns.delete_cookie('name')
    return rpns

# Signed cookies


