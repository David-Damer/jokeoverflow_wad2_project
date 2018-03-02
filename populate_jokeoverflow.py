import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jokeoverflow_wad2_project.settings')

import django

django.setup()

import jokeoverflow.models
from django.contrib.auth.models import User

def populate():

    # Create users
    users = [{'name': 'DavidDamer', 'email': '2266980d@student.gla.ac.uk', 'password': 'p@ssw0rd1'},
             {'name': 'StuartMcMillan', 'email': '2268350m@student.gla.ac.uk', 'password': 'p@ssw0rd2'},
             {'name': 'SamuelCook', 'email': '2254258h@student.gla.ac.uk', 'password': 'p@ssw0rd3'},
             {'name': 'JoeKadi', 'email': '2261087k@student.gla.ac.uk', 'password': 'p@ssw0rd4'}]

    for user in users:
        usr = User.objects.create_user(user['name'], user['email'], user['password'])
        usr.save()








if __name__ == '__main__':
    print("Starting JokeOverflow population script...")
populate()
