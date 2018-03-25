from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.decorators import login_required
from jokeoverflow.models import Category, Video, Joke, UserProfile, Comment, Voted
from jokeoverflow.forms import UserProfileForm, EditProfileForm, JokeForm, CategoryRequestForm
from jokeoverflow.forms import CommentForm, ComplaintForm
from django.shortcuts import redirect
from jokeoverflow.youtube_search import *
from django.template.defaulttags import register
from django.http import HttpResponse
from django.contrib import messages
from jokeoverflow.calculate_age import calculate_age
from django.http import JsonResponse
import json
from django.utils.timezone import now



def home(request):
    category_list = Category.objects.order_by('title')
    rec_added_videos = Video.objects.order_by('-date_added')[:5]
    all_jokes = Joke.objects.order_by('-rating')
    rated_clean_jokes = []
    for joke in all_jokes:
        if not joke.category.restricted:
            rated_clean_jokes.append(joke)
    rated_clean_short = []
    rated_clean_short = rated_clean_jokes[:5]

    all_jokes = Joke.objects.order_by('-date_added')
    recent_clean_jokes = []
    for joke in all_jokes:
        if not joke.category.restricted:
            recent_clean_jokes.append(joke)
    recent_clean_short = recent_clean_jokes[:5]

    users = UserProfile.objects.all()
    context_dict = {'categories': category_list, 'recaddedvideos': rec_added_videos, 'topratedjokes': rated_clean_short,
                    'recentjokes': recent_clean_short, 'users': users}
    response = render(request, 'jokeoverflow/home.html', context=context_dict)
    return response


def add_joke(request, category_name_slug):
    category_list = Category.objects.order_by('title')

    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = JokeForm()
    if request.method == 'POST':
        form = JokeForm(request.POST)
        user = request.user

        if form.is_valid():
            if category:
                joke = form.save(commit=False)
                joke.category = category
                joke.added_by = user
                joke.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category, 'categories': category_list}
    return render(request, 'jokeoverflow/add_joke.html', context_dict)


def about_us(request):
    category_list = Category.objects.order_by('title')
    context_dict = {'categories': category_list}
    return render(request, "jokeoverflow/about_us.html", context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    age = 0
    users = UserProfile.objects.all()
    if not request.user.is_superuser:
        if request.user.is_authenticated:
            prof = UserProfile.objects.filter(user=request.user)[0]
            age = calculate_age(prof.date_of_birth)

    try:
        category_list = Category.objects.order_by('title')
        category = Category.objects.get(slug=category_name_slug)
        rated_jokes = Joke.objects.filter(category=category).order_by('-rating')[:5]
        recent_jokes = Joke.objects.filter(category=category).order_by('-date_added')[:5]
        all_jokes = Joke.objects.filter(category=category).order_by('-upvotes')
        context_dict = {'categories': category_list, 'category': category, 'topratedjokes': rated_jokes,
                        'recentjokes': recent_jokes, 'alljokes': all_jokes, 'age': age, 'users': users}
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

def delete_user(request):
    context = {}
    u = User.objects.get(username=request.user.username)
    u.delete()      
    
    return render(request, 'jokeoverflow/delete_confirm.html', context)

@login_required
def user_profiles(request):
    userprofile = UserProfile.objects.order_by('user')
    category_list = Category.objects.order_by('title')
    users = UserProfile.objects.all().order_by('user')

    
    form = UserProfileForm(
        {'picture': UserProfile.user_picture, 'bio': UserProfile.user_bio, 'date_of_birth': UserProfile.date_of_birth})

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', request.user.username)

        else:
            print(form.errors)

    return render(request, 'jokeoverflow/user_profiles.html',
                  {'categories': category_list, 'userprofile': userprofile, 'form': form, 'users': users, })

def edit_profile(request):
    category_list = Category.objects.order_by('title')
    users = UserProfile.objects.all().order_by('user')
    userprofile = UserProfile.objects.order_by('user')
    form = EditProfileForm(request.POST or None, {'picture': UserProfile.user_picture, 'bio': UserProfile.user_bio })

    if request.method == 'POST':
        form = EditProfileForm(request.POST or None, {'picture': UserProfile.user_picture, 'bio': UserProfile.user_bio })
        if form.is_valid():
            obj = UserProfile.objects.get(user=request.user)
            obj.user_picture = form.cleaned_data['user_picture']
            obj.user_bio = form.cleaned_data['user_bio']
            obj.save()
 
            return redirect('/jokeoverflow/user_profiles/')
        else:
            print(form.errors)

    context_dict = {'categories': category_list, 'form': form, 'users':users }

    return render(request, 'jokeoverflow/edit_profile.html', context_dict)


def videos(request):
    category_list = Category.objects.order_by('title')
    rec_added_videos = Video.objects.all().order_by('-date_added')[:5]
    all_videos = Video.objects.all().order_by('title')
    context_dict = {'categories': category_list,
                    'recaddedvideos': rec_added_videos,
                    'allvideos': all_videos,
                    }
    result_list = []
    query = ''

    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            result_list = youtube_search(q=query)
    context_dict['previous_query'] = query
    context_dict['result_list'] = result_list

    response = render(request, 'jokeoverflow/videos.html', context_dict)
    return response


def top_rated_videos(request):
    category_list = Category.objects.order_by('title')
    rated_videos = Video.objects.order_by('-upvotes')[:10]
    context_dict = {'categories': category_list, 'topratedvideos': rated_videos, }
    result_list = []
    query = ''

    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            result_list = youtube_search(q=query)
    context_dict['previous_query'] = query
    context_dict['result_list'] = result_list

    response = render(request, 'jokeoverflow/videos.html', context_dict)
    return response


@login_required
def log_complaint(request):
    form = ComplaintForm()

    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()

            return redirect('home')
        else:
            print(form.errors)

    category_list = Category.objects.order_by('title')
    context_dict = {'form': form, 'categories': category_list}
    response = render(request, 'jokeoverflow/log_complaint.html', context_dict)
    return response


def top_rated_jokes(request):
    category_list = Category.objects.order_by('title')
    all_jokes = Joke.objects.order_by('-rating')
    rated_clean_jokes = []
    for joke in all_jokes:
        if not joke.category.restricted:
            rated_clean_jokes.append(joke)
    rated_clean_short = []
    rated_clean_short = rated_clean_jokes[:5]
    cat_rated_dict = {}
    for cat in category_list:
        rated_cat_jokes = Joke.objects.filter(category=cat).order_by('-rating')[:5]
        cat_rated_dict[str(cat)] = rated_cat_jokes

    form = CommentForm(request.POST)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.made_by = request.user

            comment.joke = Joke.objects.order_by('title')[0]
            comment.save()

            return redirect('home')
        else:
            print(form.errors)

    print(str(cat_rated_dict))
    comments = Comment.objects.all()
    users = UserProfile.objects.all()
    context_dict = {'categories': category_list, 'cat_rated_jokes': cat_rated_dict, 'comments': comments,
                    'topratedjokes': rated_clean_short, 'users': users, 'form': form}
    response = render(request, 'jokeoverflow/top_rated_jokes.html', context_dict)
    return response


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def search(request):
    result_list = []
    query = ''

    if request.method == 'POST':
        print('post' + query)
        query = request.POST['query'].strip()
        if query:
            result_list = youtube_search(q=query)
    context_dictionary = {'previous_query': query, 'result_list': result_list}
    return render(request, 'jokeoverflow/videos.html', context_dictionary)


def register_profile(request):
    category_list = Category.objects.order_by('title')
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

    context_dict = {'categories': category_list, 'form': form}

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
        if not Video.objects.filter(embed_code=code).exists():
            print('added')
            vid = Video.objects.get_or_create(title=title, url=url, embed_code=code,
                                              thumbnail=thumb, added_by=request.user)
        else:
            print('Not added')
            vid = Video.objects.get(embed_code=code)
            vid.date_added = now()
    videos = Video.objects.all().order_by('-date_added')[:5]
    context_dict['topratedvideos'] = videos
    return render(request, 'jokeoverflow/video_update.html', context_dict)


def testingSC1(request, jid):
    context_dict = {}

    form = CommentForm()
    joke = request.POST.get('joke')
    userget = request.GET.get('user')
    userpost = request.POST.get('user')
    userrequest = request.user
    # jokerequest = request.joke
    # jokepass = joke_slug
    joke = jid

    try:
        joke = Joke.objects.get(slug=request)
    except Joke.DoesNotExist:
        joke = None

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.joke = Joke.objects.filter(id=jid)[0]
            comment.made_by = request.user
            print(form.errors)

    context_dict = {'form': form, 'jid': jid}

    return render(request, 'jokeoverflow/testingSC1.html', context_dict)


@login_required
def upvote(request):
    joke = None
    uuser = None
    if request.method == 'GET':
        joke = request.GET['djoke']
        uuser = request.user.username

    if joke:
        upjoke = Joke.objects.get(title=joke)
        if upjoke:
            if Voted.objects.filter(user=request.user, joke=upjoke).exists():
                print('already voted')

                upvotes = upjoke.upvotes
                msg = (" You can only vote once per joke " + uuser + '!')
                return JsonResponse({"upvotes": upvotes, 'msg': msg})
            else:
                voted = Voted.objects.get_or_create(user=request.user, joke=upjoke)[0]
                voted.save()
                upvotes = upjoke.upvotes + 1
                upjoke.rating = upjoke.rating + 1
                print("vote registered")
                upjoke.upvotes = upvotes
                upjoke.save()
                msg = ("Vote Registered " + uuser + "!")
                return JsonResponse({'upvotes': upvotes, 'msg': msg})


@login_required
def downvote(request):
    joke = None
    uuser = None
    if request.method == 'GET':
        joke = request.GET['djoke']
        uuser = request.user.username
    if joke:
        downjoke = Joke.objects.get(title=joke)
        if downjoke:
            if Voted.objects.filter(user=request.user, joke=downjoke).exists():
                print('already voted')
                downvotes = downjoke.downvotes
                msg = ("You can only vote once per joke " + uuser + "!")
                return JsonResponse({"downvotes": downvotes, 'msg': msg})
            else:
                voted = Voted.objects.get_or_create(user=request.user, joke=downjoke)[0]
                voted.save()
                downvotes = downjoke.downvotes + 1
                downjoke.rating = downjoke.rating - 1
                print("vote registered")
                downjoke.downvotes = downvotes
                downjoke.save()
                msg = ("Vote Registered " + uuser + "!")
                return JsonResponse({'downvotes': downvotes, 'msg': msg})


@login_required
def add_comment(request):
    joke = None
    text = None
    if request.method == 'GET':
        joke = request.GET['joke']
        text = request.GET['text']
        if not len(text) == 0:
            cjoke = Joke.objects.get(title=joke)
            comment = Comment.objects.get_or_create(made_by=request.user, comment_text=text, joke=cjoke)[0]
            users = UserProfile.objects.all()
            context_dict = {'comment': comment, 'users': users}
            response = render(request, 'jokeoverflow/return_comment.html', context_dict)
            return response

    return HttpResponse('No comment!')


@login_required
def new_category(request):
    form = CategoryRequestForm()

    if request.method == 'POST':
        form = CategoryRequestForm(request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category = request.user
            new_category.save()

            return redirect('home')
        else:
            print(form.errors)

    category_list = Category.objects.order_by('title')
    context_dict = {'form': form, 'categories': category_list}
    response = render(request, 'jokeoverflow/new_category.html', context_dict)
    return response


def video_remove(request):
    rvideo = None
    if request.method == 'GET':
        rvideo = request.GET['video']
        vid = Video.objects.get(title=rvideo)
        vid.delete()

    return render(request, 'jokeoverflow/video_remove.html', {})


def joke_remove(request):
    rjoke = None

    if request.method == 'GET':
        rjoke = request.GET['djoke']
        joke = Joke.objects.get(title=rjoke)
        joke.delete()

    userprofile = UserProfile.objects.order_by('user')
    users = UserProfile.objects.all().order_by('user')

    return render(request, 'jokeoverflow/joke_remove.html', {'userprofile': userprofile, 'users': users})

def flag(request):
    fjoke = None
    if request.method == 'GET':
        fjoke = request.GET['fjoke']
        joke = Joke.objects.get(title=fjoke)
        if not joke.flagged:
            print('flagging')
            joke.flagged = True
            joke.save()
        else:
            print('already flagged')

    return HttpResponse('Flagged')
