from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import AbstractUser
from jokeoverflow.models import Category, Video, Joke

def home(request):

    #request.session.set_test_cookie()
    category_list = Category.objects.order_by('title')
    rated_videos = Video.objects.order_by('-upvotes')[:5]
    rated_jokes = Joke.objects.order_by('-upvotes')[:5]
    recent_jokes = Joke.objects.order_by('-date_added')[:5]
    context_dict = {'categories': category_list, 'Top Rated Videos': rated_videos, 'Top Rated Jokes': rated_jokes, 'Recent Jokes': recent_jokes, }
    #visitor_cookie_handler(request)
    response = render(request, 'jokeoverflow/home.html', context=context_dict)
    return response

def about_us(request):

    #request.session.set_test_cookie()
    #if request.session.test_cookie_worked():
    #    print("TEST COOKIE WORKED !")
    #    request.session.delete_test_cookie()
    context_dict = {'boldmessage': "I can leave a message here if required, optionally can"
                              "do it on the HTML page"}
    return render(request, "jokeoverflow/about_us.html", context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
    return render(request, 'jokeoverflow/joke_category.html', context_dict)


    
def contact_us(request):
    context_dict = {}
    response = render(request, 'jokeoverflow/contact_us.html', context_dict)
    return response

def faq(request):
    context_dict = {}
    response = render(request, 'jokeoverflow/faq.html', context_dict)
    return response

def latest_news(request):
    context_dict = {}
    response = render(request, 'jokeoverflow/latest_news.html', context_dict)
    return response

def top_rated_videos(request):
    context_dict = {}
    response = render(request, 'jokeoverflow/top_rated_videos.html', context_dict)
    return response

def top_rated_jokes(request):
    context_dict = {}
    response = render(request, 'jokeoverflow/top_rated_jokes.html', context_dict)
    return response
