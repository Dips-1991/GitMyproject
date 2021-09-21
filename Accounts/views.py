from django.shortcuts import render

# Create your views here.

def Add(request):
    
    num1= int(request.POST['num1'])
    num2= int(request.POST['num2'])
    
    res = num1 + num2
    
    return render(request,"Res.html",res)