from django import forms
from jokeoverflow.models import UserProfile, Joke, Video, Comment, Category, Complaint, CategoryRequest
from django.contrib.auth.models import User
from django.utils.timezone import now


class UserProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1960, now().year + 1)))
    user_bio = forms.CharField(widget=forms.Textarea, max_length=256, required=False)
    user_picture = forms.ImageField(required=False)
    image_from = forms.URLField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = UserProfile
        exclude = ('user',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class JokeForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='Give the joke a title.')
    joke_text = forms.CharField(widget=forms.Textarea, max_length=256, help_text='Tell us your joke!')
    date_added = forms.DateTimeField(widget=forms.HiddenInput, required=False)
    upvotes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    downvotes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    flagged = forms.BooleanField(widget=forms.HiddenInput, initial=False, required=False)

    class Meta:
        model = Joke
        fields = ('title', 'joke_text')


class VideoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea, max_length=128, help_text='What\'s the video called?')
    url = forms.URLField(max_length=200, help_text='Please enter the url of the video.')
    upvotes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    downvotes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    rating = forms.IntegerField(widget=forms.HiddenInput, initial=0)

    class Meta:
        model = Video
        exclude = ('added_by', 'date_added', 'thumbnail')


class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(max_length=256, help_text='Please enter your comments...', widget=forms.TextInput)

    class Meta:
        model = Comment
        exclude = ('made_by', 'joke', 'date_added')



class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the category name.")
    restricted = forms.BooleanField(widget=forms.HiddenInput(), initial=False)
    no_of_jokes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Category
        fields = ('title',)


class ComplaintForm(forms.ModelForm):
    complaint = forms.CharField(widget=forms.Textarea, max_length=256)

    class Meta:
        model = Complaint
        exclude = ('user', 'date_added')

class CategoryRequestForm(forms.ModelForm):
    new_category = forms.CharField(max_length=128, help_text="Please enter the new category name.")

    class Meta:
        model = CategoryRequest
        exclude = ('user', 'date_added')

    
