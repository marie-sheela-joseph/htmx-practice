
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "app1/template1.html", {"test": 'test1'})

def test(request):
    return render(request, "app1/test.html", {"test_data": 'This is a test'})

def test_put(request, id):
    print("request",request,"id",id)
    return HttpResponse("hello post request")