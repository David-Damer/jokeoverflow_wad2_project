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

def register(request):

    if request.session.test_cookie_worked():
        print("TEST COOKIE WORKED !")
        request.session.delete_test_cookie()
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        bio_form = models.TextField(max_length=500, blank=True)
        bio_form = UserBioForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            bio = bio_form.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        bio_form = UserBioForm()
    return render(request, 'jokeoverflow/register.html', {'user_form': user_form,
                                                          'profile_form': profile_form,
                                                          'bio_form' : bio_form,
                                                          'registered': registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            context_dict = {}
            usr = User.objects.filter(username=username)
            if user == '' or not usr:
                context_dict['error'] = "Wronguser"
            else:
                if password == '':
                    context_dict['error'] = "Please enter the correct password"
                else:
                    context_dict['error'] = "Wrong Password"

            return render(request, 'jokeoverflow/login.html', context_dict)
    else:
        return render(request, 'jokeoverflow/login.html', {})

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
    return render(request, 'rango/category.html', context_dict)


    
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
