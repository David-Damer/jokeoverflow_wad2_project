from django.contrib import admin
from jokeoverflow.models import Category, Video, UserProfile, Joke, Comment

# Register your models here.
admin.site.register(Category, Video, UserProfile, Joke, Comment)
