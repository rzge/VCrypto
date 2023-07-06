from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    friends = models.ManyToManyField('CustomUser', blank=True, symmetrical=True)
    bitcoin_address = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.username


# class FriendList(models.Model):
#     user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='user')
#     friends = models.ManyToManyField('CustomUser', blank=True, related_name='friends')
#
#     def __str__(self):
#         return self.user.username
#
#     def add_friend(self, account):
#         if not account in self.friends.all():
#             self.friends.add(account)
#
#     def remove_friend(self, account):
#         if account in self.friends.all():
#             self.friends.remove(account)
#
#     def unfriend(self, removee):
#         # removee - пользователь, которого будут убирать из друзей
#         remover_friends_list = self  # тот, кто уничтожает дружбу
#         remover_friends_list.remove_friend(removee)  # убираем пользователя из списка друзей
#         friends_list = FriendList.objects.get(
#             user=removee)  # убираем себя из друзей у пользователя, с кем разорвали дружбу
#         friends_list.remove_friend(remover_friends_list.user)
#
#     def is_mutual_friend(self, friend):  # проверка, а я являемся ли мы друзьями
#         if friend in self.friends.all():
#             return True
#         return False


class FriendRequest(models.Model):
    sender = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='receiver')
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username

    # def accept(self):
    #     receiver_friend_list = FriendList.objects.get(user=self.receiver)
    #     if receiver_friend_list:
    #         receiver_friend_list.add_friend(self.sender)
    #         sender_friend_list = FriendList.objects.get(user=self.sender)
    #         if sender_friend_list:
    #             sender_friend_list.add_friend(self.receiver)
    #             self.is_active = False
    #             self.save()  # вроде необязательно
    #
    # def decline(self):
    #     # нужно поле is_active в false
    #     self.is_active = False
    #     self.save()

# Create your models here.


# Create your models here.
