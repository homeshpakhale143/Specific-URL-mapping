from django.shortcuts import render

# Create your views here.
def send_data(request):
    d={'name':'HOMESH','age':25}
    return render(request,'send_data.html',context=d)