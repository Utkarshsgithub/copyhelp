from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as loginUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from copyapp.forms import COPYForm

def home(request):
    return render(request, 'html/index.html')

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form": form,
            "hi": True
        }
        return render(request, 'html/login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('workspace')
        else:
            context = {
                "form": form,
                "hi": True
            }
            return render(request, 'html/login.html', context=context)

def register(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form": form,
            "error": True
        }
        return render(request, 'html/register.html', context=context)
    else:
        form = UserCreationForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'html/register.html', context=context)

def workspace(request):
    form = COPYForm()
    return render(request, 'html/workspace.html', context={'form':form})

def add_copy(request):
    user = request.user
    form = COPYForm(request.POST)
    if form.is_valid():
        copy = form.save(commit=False)
        copy.user = user
        copy.save()
        return redirect('workspace')
    else:
        return render(request, 'html/index.html', context={'form':form})