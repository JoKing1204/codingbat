from django.shortcuts import render

from django.http.request import HttpRequest
from django.http.response import HttpResponse


def warmup_1(request: HttpRequest, n) -> HttpResponse:
   return HttpResponse((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

def warmup_2(request: HttpRequest, res) -> HttpResponse:
    result = ""
    for i in range(len(res)):
        result = result + res[:i + 1]
    return HttpResponse(result)


def string_2(request: HttpRequest, c) -> HttpResponse:
    count1 = 0
    count2 = 0
   
    if 'dog' and 'cat' not in c:
        return HttpResponse(True)
    for i in range(len(c)-1):
        if c[i:i+3] == 'cat':
            count1 += 1
        if c[i:i+3] == 'dog':
            count2 += 1
    if count1 == count2:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def logic_2(request: HttpRequest, a, b, c) -> HttpResponse:
    
  if a==b==c:
    return HttpResponse(0)
  elif a==b:
    return HttpResponse(c)
  elif b==c:
    return HttpResponse(a)
  elif c==a:
    return HttpResponse(b)
  elif a!=b!=c:
    return HttpResponse(a+b+c)
