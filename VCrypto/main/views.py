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
        return HttpResponse('Отправлен запрос дружбы')
    else:
        return HttpResponse('Запрос дружбы уже был отправлен')

@login_required
def cancel_friend_request(request, userID): #отменяет отправленный запрос дружбы
    sender = request.user
    receiver = models.CustomUser.objects.get(id=userID)
    print(sender)
    print(receiver)
    if models.FriendRequest.objects.filter(sender=sender, receiver=receiver).delete()[0] != 0:
        return HttpResponse('Запрос дружбы отменён')
    else:
        return HttpResponse('Запрос дружбы уже был отменён')

    #
    # return redirect('profile', to_user_id)

    # unfriended_user = models.CustomUser.objects.get(id=userID)
    # friend_request = models.FriendRequest.objects.get(receiver=unfriended_user)
    # print(friend_request.receiver.id)
    # #friend_request.delete()
    # if request.user == friend_request.from_user:
    #     friend_request.delete()
    #     return redirect('user_profile', user_id=friend_request.to_user.id)
    # else:
    #     return redirect('home')

def pageNotFound(request, exception):
    return render(request, 'main/404.html')

# функции, для отработки логики дружбы
