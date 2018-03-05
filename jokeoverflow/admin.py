from django.contrib import admin
from jokeoverflow.models import Category, Video
from jokeoverflow.models import UserProfile, Joke, Comment
# Register your models here.
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Video)
admin.site.register(Joke)

