from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User Model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include
    date_of_birth = models.DateField(blank=False)
    user_bio = models.TextField(max_length=256)
    user_picture = models.ImageField(upload_to='profile_images')
    image_from = models.URLField()  # For acknowledging sources of images when populating with fake data
  
    def __str__(self):
        return self.user.username

        
class Video(models.Model):
    title = models.CharField(max_length=128, unique=True)
    added_by = models.ForeignKey(User, related_name='videos')
    url = models.URLField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    embed_code = models.CharField(max_length=60)
    thumbnail = models.URLField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=128)
    restricted = models.BooleanField()
    no_of_jokes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Joke(models.Model):
    title = models.CharField(max_length=128)
    joke_text = models.TextField(max_length=256)
    date_added = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    flagged = models.BooleanField(default=False)
    category = models.ForeignKey(Category)
    added_by = models.ForeignKey(User, related_name='jokes')
    rating = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Joke, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_text = models.TextField(max_length=64, unique=False)
    made_by = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_now_add=True)
    joke = models.ForeignKey(Joke, related_name='comments')

    def __str__(self):
        return self.comment_text


class Voted(models.Model):
    joke = models.ForeignKey(Joke)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.joke.title + " : Voted on by " + self.user.username


class Complaint(models.Model):
    user = models.ForeignKey(User)
    complaint = models.TextField(max_length=256, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.complaint

class CategoryRequest(models.Model):
    user = models.ForeignKey(User)
    new_category = models.CharField(max_length=128, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.new_category
