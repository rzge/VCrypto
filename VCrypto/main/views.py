from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'main/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'main/about_you.html') #возможность видеть личную информацию

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Не найдено(</h1>')