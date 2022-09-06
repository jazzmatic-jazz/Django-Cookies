from django.urls import path
from .views import (setcookie, getcookie, 
                    delcookie, setsignedcookie,
                    getsignedcookie)

urlpatterns =[
    path('set/', setcookie),
    path('get/', getcookie),
    path('del/', delcookie),
    
# Signed cookies
    path('setsigned/', setsignedcookie),
    path('getsigned/', getsignedcookie),

]