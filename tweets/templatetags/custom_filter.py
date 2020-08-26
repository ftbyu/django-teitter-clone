from django import template
from django.utils.safestring import mark_safe
from ..models import Like
register = template.Library()


@register.filter(name='get_likes')
def get_likes(like_list, key):
    text = ""
    if key in like_list:
        text = ""
        for like in like_list[key]:
            text += f"{like.user.username}, "
            text += "がいいねしました"
    return text

@register.filter(name='is_like')
def is_like(tweet, user):
    if Like.objects.filter(user=user, tweet=post).exists():
        return mark_safe(f"<button class=\"like\" id=\"{tweet.id}\" type=\"submit\"><i class=\" fas fa-heart\"></i></button>")
    else:
        return mark_safe(f"<button class=\"like\" id=\"{tweet.id}\" type=\"submit\"><i class=\" far fa-heart\"></i></button>")
