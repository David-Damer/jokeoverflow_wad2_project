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

    # Comment this block out if you make changes to the script
    # we can't create the same user twice; we get a uniqueness error!
    # Uncomment this the first time you run populate_jokeoverflow
    # for user in users:
    #     usr = User.objects.create_user(user['name'], user['email'], user['password'])
    #     usr.save()

    # Create User profiles for users
    for user in users:
        up = add_profile(user=user['name'],date_of_birth=user['date_of_birth'])
        up.user_bio = user['user_bio']
        up.save()






def add_profile(user, date_of_birth):
    up = UserProfile.objects.get_or_create(user__username=user,date_of_birth=date_of_birth)[0]
    # we need to save the changes we made!!
    up.save()
    return up





if __name__ == '__main__':
    print("Starting JokeOverflow population script...")
populate()
