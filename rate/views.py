from django.shortcuts import render,redirect
from .models import Project
from .forms import RegisterForm
from django.contrib import messages



def index(request):

    posts = Project .objects.all()

    return render(request, 'index.html', {"posts":posts})



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            

            messages.success(request, f'Account {username} created')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request , 'registration/register.html', {'form':form})