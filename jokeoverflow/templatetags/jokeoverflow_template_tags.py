from django import template
from jokeoverflow.models import Joke,UserProfile

register = template.Library()

@register.inclusion_tag('jokeoverflow/jokes.html')
def get_joke_pop(joke=None, user=None):
    return {'jokes':Joke.objects.all(),
            'act_joke': joke,
            'users': UserProfile.objects.all(),
            'act_user': user,
            }
