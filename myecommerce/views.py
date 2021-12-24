from django.shortcuts import render

def home(request):
    #render(request, template_name, context=None, content_type=None, status=None, using=None)
    return render(request,'index.html')