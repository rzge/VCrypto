from django import template
from users.models import *
register = template.Library()


@register.simple_tag()
def get_friend_requests():
    return [x['receiver'] for x in FriendRequest.objects.values('receiver')]
