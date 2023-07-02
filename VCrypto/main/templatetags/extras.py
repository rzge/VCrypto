from django import template
from users.models import *
register = template.Library()


@register.simple_tag()
def get_friend_requests_receiver():
    return [x['receiver'] for x in FriendRequest.objects.values('receiver')]

@register.simple_tag()
def get_friend_requests_sender():
    return [x['sender'] for x in FriendRequest.objects.values('sender')]