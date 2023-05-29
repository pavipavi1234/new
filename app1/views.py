from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'pavu'}
    return render(request,'wish.html',context=d)
