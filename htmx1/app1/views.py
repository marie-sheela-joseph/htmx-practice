
from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

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

# languages() version 3 - split languages into 2 end points activate, deactivate 
LANGUAGES={"python":True,"javascript":True,"c":False}
def bulk_update(request):    
    return render(request, "app1/bulk_update.html",{'languages':LANGUAGES})

def activate(request):
    selected_languages=request.POST.getlist("lang")
    for key,value in LANGUAGES.items():
        if key in selected_languages:
            LANGUAGES[key]=True
        else:
            LANGUAGES[key]=False
    print(LANGUAGES)
    return render(request, "app1/partials/languages.html",{"languages":LANGUAGES})

def deactivate(request):
    selected_languages=request.POST.getlist("lang")
    for key,value in LANGUAGES.items():
        if key in selected_languages:
            LANGUAGES[key]=False        
    print(LANGUAGES)
    return render(request, "app1/partials/languages.html",{"languages":LANGUAGES})

# languages() version 2 with dictionary
# LANGUAGES={"python":True,"javascript":True,"c":False}
# def languages(request):
#     selected_languages=request.POST.getlist("lang")
#     for key,value in LANGUAGES.items():
#         if key in selected_languages:
#             LANGUAGES[key]=True
#         else:
#             LANGUAGES[key]=False
#     print(LANGUAGES)
#     return render(request, "app1/partials/languages.html",{"languages":LANGUAGES})

# languages() version 1
# def languages(request):
#     selected_languages=request.POST.getlist("lang")
#     return render(request, "app1/partials/languages.html",{"selected_languages":selected_languages})

# bulk update
# def bulk_update(request):    
#     return render(request, "app1/bulk_update.html",{'selected_languages':selected_languages})

contacts=[{"id":1,"first_name":"A","percentage":90
}]

# class based views
class ContactView(TemplateView):
    template_name="app1/contact.html"

    def get_context_data(self,**kwargs):
        if self.request.method=="GET":            
            id=kwargs["id"]            
            current_contact={}
            for c in contacts:
                if c["id"]==id:
                    current_contact=c                      
            return {'contact':current_contact}
        if self.request.method=="PUT":
            print(kwargs)        
            id=kwargs["id"]            
            current_contact={}
            for c in contacts:
                if c["id"]==id:
                    c["first_name"]=kwargs["first_name"]
                    c["percentage"]=kwargs["percentage"]
                    current_contact=c
            return {'contact':current_contact}
        
        
# function based views
# def contact(request,id):   
#     if request.method=="GET":
#         print("get req")
#         current_contact={}
#         for c in contacts:
#             if c["id"]==id:
#                 current_contact=c     
#         return render(request, "app1/contact.html",{'contact':current_contact})
    
#     if request.method=="PUT" :
#         print("put req")
#         current_contact={}
#         for c in contacts:
#             if c["id"]==id:
#                 c["first_name"]=request.PUT.get("first_name")
#                 c["percentage"]=request.PUT.get("percentage")
#                 current_contact=c
#         return render(request, "app1/contact.html",{'contact':current_contact})        
    
# class based view
class ContactForm(TemplateView):
    template_name="app1/contact_form.html"

    def get_context_data(self, **kwargs):
        if self.request.method=="GET":
            id=kwargs["id"]
            current_contact={}
        for c in contacts:
            if c["id"]==id:
                current_contact=c 
        return {"contact":current_contact}
    
# function based view
# def contact_form(request,id):
#     current_contact={}
#     for c in contacts:
#         if c["id"]==id:
#             current_contact=c    
#     return render(request,"app1/contact_form.html",{"contact":current_contact})