from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import AbstractUser
from jokeoverflow.models import Category, Video, Joke
from jokeoverflow.forms import UserProfileForm

def home(request):
    category_list = Category.objects.order_by('title')
    rated_videos = Video.objects.order_by('-upvotes')[:5]
    rated_jokes = Joke.objects.order_by('-upvotes')[:5]
    recent_jokes = Joke.objects.order_by('-date_added')[:5]
    context_dict = {'categories': category_list, 'topratedvideos': rated_videos, 'topratedjokes': rated_jokes, 'recentjokes': recent_jokes, }
    response = render(request, 'jokeoverflow/home.html', context=context_dict)
    return response

def about_us(request):
    
    category_list = Category.objects.order_by('title')
    context_dict = {'categories': category_list}
    return render(request, "jokeoverflow/about_us.html", context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category_list = Category.objects.order_by('title')
        category = Category.objects.get(slug=category_name_slug)
        rated_jokes = Joke.objects.filter(category=category).order_by('-upvotes')[:5]
        recent_jokes = Joke.objects.filter(category=category).order_by('-date_added')[:5]
        context_dict = {'categories': category_list, 'category': category, 'topratedjokes': rated_jokes, 'recentjokes': recent_jokes, }
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['topratedjokes'] = None

    return render(request, 'jokeoverflow/joke_category.html', context = context_dict)


 
    
def contact_us(request):
    category_list = Category.objects.order_by('title')
    context_dict = {'categories': category_list}
    response = render(request, 'jokeoverflow/contact_us.html', context_dict)
    return response

def faq(request):
    category_list = Category.objects.order_by('title')
    context_dict = {'categories': category_list}
    response = render(request, 'jokeoverflow/faq.html', context_dict)
    return response

def latest_news(request):
    category_list = Category.objects.order_by('title')
    context_dict = {'categories': category_list}
    response = render(request, 'jokeoverflow/latest_news.html', context_dict)
    return response

def top_rated_videos(request):
    category_list = Category.objects.order_by('title')
    rated_videos = Video.objects.order_by('-upvotes')[:5]
    context_dict = {'categories': category_list, 'topratedvideos' : rated_videos}
    response = render(request, 'jokeoverflow/top_rated_videos.html', context_dict)
    return response

def top_rated_jokes(request):
    category_list = Category.objects.order_by('title')
    rated_jokes = Joke.objects.order_by('-upvotes')[:5]
    context_dict = {'categories': category_list, 'topratedjokes' : rated_jokes}
    response = render(request, 'jokeoverflow/top_rated_jokes.html', context_dict)
    return response

