from django import template
from users.models import *

register = template.Library()


@register.simple_tag()
def get_friend_requests_receiver():  # показывает всех получателей
    return [x['receiver'] for x in FriendRequest.objects.values('receiver')]


@register.simple_tag()
def get_friend_requests_sender():  # показывает всех отправителей
    return [x['sender'] for x in FriendRequest.objects.values('sender')]


@register.simple_tag(name='receivers')
def receivers_list(user_id=None):  # показывает получателей от конкретного юзера
    receiver_ids = FriendRequest.objects.filter(sender=user_id).values_list('receiver', flat=True)
    return receiver_ids

@register.simple_tag(name='senders')
def senders_list(user_id=None):  # показывает получателей от конкретного юзера
    sender_ids = FriendRequest.objects.filter(receiver=user_id).values_list('sender', flat=True)
    return sender_ids