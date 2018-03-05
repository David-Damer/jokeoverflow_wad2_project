from django import forms
from jokeoverflow.models import UserProfile, Joke, Video, Comment, Category, Voted
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):

    date_of_birth = forms.DateField(required=True)
    user_bio = forms.TextField(max_length=256, required=False)
    user_picture = forms.ImageField(upload_to='profile_images', required=False)
    image_from = forms.URLField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = UserProfile
        exclude = ('user',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')