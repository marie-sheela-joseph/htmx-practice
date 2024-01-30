
from django.shortcuts import render

def index(request):
    return render(request, "app1/template1.html", {"test": 'test1'})

def test(request):
    return render(request, "app1/test.html", {"test_data": 'This is a test'})
