
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "app1/template1.html", {"test": 'test1'})

def test(request):
    return render(request, "app1/test.html", {"test_data": 'This is a test'})

# test_post
# def test_post(request, id):
#     print("request",request,"id",id, "first_name", request.POST.get("first_name"),"last_name", request.POST.get("last_name"))
#     return HttpResponse(f'Hello {request.POST.get("first_name")} {request.POST.get("last_name")}')

# args , kwargs
# def test_post(request, *args,**kwargs):
#     print("request",request,"args",args,"kwargs",kwargs, "first_name", request.POST.get("first_name"),"last_name", request.POST.get("last_name"))
#     return HttpResponse(f'Hello {request.POST.get("first_name")} {request.POST.get("last_name")}')

# kwargs["a"] vs kwargs.get("a")
# get values from kwargs using kwargs["a"]
def test_post(request, *args,**kwargs):
    print("request",request,"\n args",args,"\n kwargs",kwargs, "\n kwargs['a']",kwargs["a"],"\n first_name", request.POST.get("first_name"),"\n last_name", request.POST.get("last_name"))
    return HttpResponse(f'Hello {request.POST.get("first_name")} {request.POST.get("last_name")}')

# get values from kwargs using kwargs.get("a")
def test_post(request, *args,**kwargs):
    print("request",request,"\n args",args,"\n kwargs",kwargs, "\n kwargs.get('a')",kwargs.get("a"),"\n first_name", request.POST.get("first_name"),"\n last_name", request.POST.get("last_name"))
    return HttpResponse(f'Hello {request.POST.get("first_name")} {request.POST.get("last_name")}')

# bulk update
def bulk_update(request):    
    selected_languages=request.POST.getlist('lang')
    print(request.POST,request.POST.getlist('lang'),selected_languages)
    return render(request, "app1/bulk_update.html",{'selected_languages':selected_languages})