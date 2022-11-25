from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':10,'b':20}
    return render(request,'a1_first.html',d)
def a1_second(request):
    e={'a':10,'b':20,'c':30}
    return render(request,'a1_second.html',e)
def a2_first(request):
    d={'a':10,'b':21,'c':30,'d':40}
    return render(request,'a2_first.html',d)
