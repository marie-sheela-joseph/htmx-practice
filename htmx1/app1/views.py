# from django.http import HttpResponse

# def index(request):
#     return HttpResponse('hello django')


from django.shortcuts import render

def index(request):
    return render(request, "app1/template1.html", {"test": 'test1'})
    
def test(request):
    return render(request, "app1/test.html", {"test": 'test1'})
  
# class test(request):
#     template_name="app1/test.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["test"] = "test1"
#         return context
    