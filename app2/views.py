from django.shortcuts import render

# Create your views here.
def a2_second(request):
    d={'name':'ashu'}
    return render(request,'a2_second.html',d)
