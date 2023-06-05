from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users import models

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
    return render(request, 'main/about_you.html')  # возможность видеть личную информацию


def search_results(request):  # поисковая строка
    query = request.GET.get('query')
    if not query:
        query = ""
    results = models.CustomUser.objects.filter(username__icontains=query)
    print(results)
    return render(request, 'main/search_results.html', {'results': results, 'query': query})

@login_required
def send_friend_request(request, userID):
    sender = request.user
    receiver = models.CustomUser.objects.get(id=userID)
    friend_request, created = models.FriendRequest.objects.get_or_create(sender=sender, receiver=receiver)
    if created:
        return HttpResponse('friend request sent')
    else:
        return HttpResponse('friend request was already sent')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Не найдено(</h1>')

# функции, для отработки логики дружбы
