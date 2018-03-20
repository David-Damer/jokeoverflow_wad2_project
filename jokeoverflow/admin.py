from django.contrib import admin
from jokeoverflow.models import Category, Video
from jokeoverflow.models import UserProfile, Joke, Comment, Complaint

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class JokeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Video)
admin.site.register(Joke, JokeAdmin)
admin.site.register(Complaint)

