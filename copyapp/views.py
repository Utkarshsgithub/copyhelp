from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(request):
    return render(request, 'html/index.html')

def login(request):
    form = AuthenticationForm()
    context = {
        "from": form
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


