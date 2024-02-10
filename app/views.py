from django.shortcuts import render

# Create your views here.

from app.forms import userform,myform

from app.models import user

from django.http import HttpResponse


def home(request):
    uf = userform()


    if request.method == 'POST' and request.FILES:
        ufd = userform(request.POST,request.FILES)
        print(ufd)
        if ufd.is_valid():
            ufd.save()
            return HttpResponse("data is valid")
            
        else:
            print(ufd.errors)

            return HttpResponse("data is not valid")

        return HttpResponse("data is getting")


    return render(request,'form.html',{'uf':uf})


def user_form(request):
    mf = myform()

    if request.method == 'POST':
        mfd = myform(request.POST)
        pw = request.POST['password']
        if mfd.is_valid():

            umd = mfd.save(commit=False) #this is act as a temporary data base 

            umd.set_password(pw)

            umd.save()

            return HttpResponse("data stored successfully")




    return render(request,'user_form.html',{'mf':mf})



