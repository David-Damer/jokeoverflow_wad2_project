from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify 

# Create your models here.

class UserProfile(models.Model):

    # This line is required. Links UserProfile to a User Model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include
    date_of_birth = models.DateField(blank=False)
    user_bio = models.CharField(max_length=256, blank=True)
    user_picture = models.ImageField(upload_to='profile_images', blank=True)
    image_from = models.URLField()  # For acknowledging sources of images when populating with fake data
    
    def __str__(self):
        return self.user.username
    
class Video(models.Model):
    
    title = models.CharField(max_length=128, unique=True)
    added_by = models.OneToOneField(User)
    link = models.URLField()
    added_date = models.DateField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    
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
    

#  OneToOneField classes used to automatically become the primary key on a model.
#  This is no longer true (although you can manually pass in the primary_key argument if you like). 
#  Thus, it’s now possible to have multiple fields of type OneToOneField on a single model.

class Joke(models.Model):
    
    title = models.CharField(max_length=128)
    joke_text = models.CharField(max_length=256)
    date_added = models.DateField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    flagged = models.BooleanField(default=False)
    category = models.OneToOneField(Category)
    added_by = models.OneToOneField(User)
    
    def __str__(self):
        return self.title

    
class Comment(models.Model):
    
    comment_text = models.CharField(max_length=256)
    made_by = models.OneToOneField(User)
    date_added = models.DateField()
    joke = models.OneToOneField(Joke)
    
    def __str__(self):
        return self.comment_text
    