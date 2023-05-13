from django.shortcuts import render
from django.contrib.auth import authenticate,login
from .form import LoginForm
from django.http import HttpResponse
# Create your views here.


def loginn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,
                              username=cd['username'],
                              password =cd['password'])
            
            if user is not None:
                login(request, user)
                return HttpResponse('Login Successfull')
            else:
                return HttpResponse('login failed')
    else :
        form=LoginForm()

    return render(request,'login.html',{'form':form})