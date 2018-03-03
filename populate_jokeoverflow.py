import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jokeoverflow_wad2_project.settings')

import django

django.setup()

from jokeoverflow.models import UserProfile, Comment, Joke, Video, Category
from django.contrib.auth.models import User

def populate():

    # Create users
    users = [{'name': 'DavidDamer', 'email': '2266980d@student.gla.ac.uk', 'password': 'p@ssw0rd1',
              'date_of_birth': '1975-05-07', 'user_bio': 'Just me'},
             {'name': 'StuartMcMillan', 'email': '2268350m@student.gla.ac.uk', 'password': 'p@ssw0rd2',
              'date_of_birth': '1987-12-10', 'user_bio': 'Just Stuart'},
             {'name': 'SamuelCook', 'email': '2254258h@student.gla.ac.uk', 'password': 'p@ssw0rd3',
              'date_of_birth': '1994-02-16', 'user_bio': 'Just Sam'},
             {'name': 'JoeKadi', 'email': '2261087k@student.gla.ac.uk', 'password': 'p@ssw0rd4',
              'date_of_birth': '1994-04-06', 'user_bio': 'Just Joe'}]

    for user in users:
        username = user['name']
        email = user['email']
        password = user['password']
        dob = user['date_of_birth']
        bio = user['user_bio']
        usr = add_user(username, email, password)
        usrprof = add_profile(user = usr,date_of_birth = dob, user_bio =  bio)


def add_profile(user, date_of_birth, user_bio):
    up = UserProfile.objects.get_or_create(user=user, date_of_birth=date_of_birth)[0]
    up.user_bio = user_bio
    up.save()
    return up

def add_user(name, email, password):
    user = User.objects.get_or_create(username=name, email=email, password=password)[0]
    return user



if __name__ == '__main__':
    print("Starting JokeOverflow population script...")
    populate()
