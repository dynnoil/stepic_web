#-*-coding: utf-8-*-

from django.shortcuts import render
from django.http import HttpResponse

def test(request, *args, **kwargs): 
    # в аргумент *args попадают позиционные параметры роутера
    # в аргумент **kwargs попадают именованные параметры роутера
    return HttpResponse('OK')
