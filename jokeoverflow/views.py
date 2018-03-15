from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required
from jokeoverflow.models import Category, Video, Joke, UserProfile, Comment
from jokeoverflow.forms import UserProfileForm
from django.shortcuts import redirect
from jokeoverflow.youtube_search import *



def home(request):
    category_list = Category.objects.order_by('title')
    rated_videos = Video.objects.order_by('-rating')[:5]
    rated_jokes = Joke.objects.order_by('-rating')[:10]
    recent_jokes = Joke.objects.order_by('-date_added')[:10]
    context_dict = {'categories': category_list, 'topratedvideos': rated_videos, 'topratedjokes': rated_jokes,
                    'recentjokes': recent_jokes, }
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
        rated_jokes = Joke.objects.filter(category=category).order_by('-rating')[:2]
        recent_jokes = Joke.objects.filter(category=category).order_by('-date_added')[:2]
        all_jokes = Joke.objects.filter(category=category).order_by('-upvotes')
        context_dict = {'categories': category_list, 'category': category, 'topratedjokes': rated_jokes,
                        'recentjokes': recent_jokes, 'alljokes': all_jokes, }
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['topratedjokes'] = None
        context_dict['categories'] = None
        context_dict['recentjokes'] = None

    return render(request, 'jokeoverflow/joke_category.html', context=context_dict)


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

def user_profiles(request):
    category_list = Category.objects.order_by('title')
    user_profiles = UserProfile.objects.order_by('user')
    context_dict = {'categories': category_list, 'user_profiles': user_profiles}
    response = render(request, 'jokeoverflow/user_profiles.html', context_dict)
    return response


def top_rated_videos(request):
    category_list = Category.objects.order_by('title')
    rated_videos = Video.objects.order_by('-upvotes')[:10]
    context_dict = {'categories': category_list, 'topratedvideos': rated_videos,}
    result_list = []
    query = ''

    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            result_list = youtube_search(q=query)
    context_dict['previous_query'] = query
    context_dict['result_list'] = result_list

    response = render(request, 'jokeoverflow/top_rated_videos.html', context_dict)
    return response

def log_complaint(request):
    category_list = Category.objects.order_by('title')
    context_dict = {'categories': category_list}
    response = render(request, 'jokeoverflow/log_complaint.html', context_dict)
    return response


def top_rated_jokes(request):
    category_list = Category.objects.order_by('title')
    rated_jokes = Joke.objects.order_by('-upvotes')[:5]
    comments = Comment.objects.all()
    users = UserProfile.objects.all()
    context_dict = {'categories': category_list, 'comments': comments, 'topratedjokes': rated_jokes, 'users': users}
    response = render(request, 'jokeoverflow/top_rated_jokes.html', context_dict)
    return response


def search(request):
    result_list = []
    query = ''

    if request.method == 'POST':
        print('post' + query)
        query = request.POST['query'].strip()
        if query:
            result_list = youtube_search(q=query)
    context_dictionary = {'previous_query': query, 'result_list': result_list}
    return render(request, 'jokeoverflow/top_rated_videos.html', context_dictionary)

def register_profile(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect('home')
        else:
            print(form.errors)

    context_dict = {'form':form}

    return render(request, 'jokeoverflow/register_profile.html', context_dict)



@login_required
def auto_add_video(request):
    url = None
    code = None
    thumb = None
    title = None
    context_dict = {}

    if request.method == 'GET':
        title = request.GET['title']
        url = request.GET['url']
        code = request.GET['code']
        thumb = request.GET['thumb']
        print('added')
        vid = Video.objects.get_or_create(title=title, url=url, embed_code=code,
                                          thumbnail=thumb, added_by=request.user)
        videos = Video.objects.order_by('-upvotes')[:10]
        category_list = Category.objects.order_by('title')
        context_dict = {'categories': category_list, 'topratedvideos': videos, }

        return render(request, 'jokeoverflow/top_rated_videos.html', context_dict)
