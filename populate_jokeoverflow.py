import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jokeoverflow_wad2_project.settings')

import django

django.setup()

from jokeoverflow.models import UserProfile, Comment, Joke, Video, Category
from django.contrib.auth.models import User



def populate():
    # Create users
    users = [
        {'name': 'DavidDamer', 'email': '2266980d@student.gla.ac.uk', 'password': 'p@ssw0rd1',
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
        usrprof = add_profile(user=usr, date_of_birth=dob, user_bio=bio)

    knock_knock_jokes = [
        {'title': 'Dr who joke', 'text': 'Knock knock.\nWho\'s there?\nDr.\nDr who?\nNo, Dr Jones.',
         'date_added': '2018-01-01',
         'upvotes': 5, 'downvotes': 7, 'added_by': 'JoeKadi'},
        {'title': 'Canoe Joke',
         'text': 'Knock knock.\nWho\'s there?\nCanoe.\nCanoe who?\nCanoe help with my homework?.',
         'date_added': '2018-01-01',
         'upvotes': 10, 'downvotes': 2, 'added_by': 'SamuelCook'},
        {'title': 'Iva Joke',
         'text': 'Knock knock.\nWho\'s there?\nIva.\nIva who?\nIva sore hand from knocking.',
         'date_added': '2018-01-01',
         'upvotes': 12, 'downvotes': 9, 'added_by': 'StuartMcMillan'},
    ]

    yo_mama_jokes = [
        {'title': 'Fat mama joke', 'text': 'Yo mama so fat, she doesn\'t need the internet; she already world wide!',
         'date_added': '2018-01-01',
         'upvotes': 5, 'downvotes': 7, 'added_by': 'DavidDamer'},
        {'title': 'Hockey Joke',
         'text': 'Yo mama is like a hockey player, she only showers after three periods.',
         'date_added': '2018-01-01',
         'upvotes': 3, 'downvotes': 5, 'added_by': 'SamuelCook'},
        {'title': 'Ugly Joke',
         'text': 'Yo mama so ugly, she tried to enter an ugliness competition and they said "No professionals".',
         'date_added': '2018-01-01',
         'upvotes': 9, 'downvotes': 5, 'added_by': 'StuartMcMillan'}
    ]

    chuck_norris_jokes = [
        {'title': 'Death', 'text': 'Death once had a near Chuck experience',
         'date_added': '2018-01-01',
         'upvotes': 5, 'downvotes': 7, 'added_by': 'DavidDamer'},
        {'title': 'Street',
         'text': 'There used to be a street named after Chuck Norris. They had to change the name because nobody crosses Chuck Norris and lives.',
         'date_added': '2018-01-01',
         'upvotes': 44, 'downvotes': 1, 'added_by': 'JoeKadi'},
        {'title': 'Guns',
         'text': 'Guns carry Chuck Norris for protection.',
         'date_added': '2018-01-01',
         'upvotes': 11, 'downvotes': 8, 'added_by': 'StuartMcMillan'}
    ]

    dad_jokes = [
        {'title': 'Hungry', 'text': 'Dad, I\'m hungry...\nHi hungry I\'m dad',
         'date_added': '2018-01-01',
         'upvotes': 5, 'downvotes': 7, 'added_by': 'DavidDamer'},
        {'title': 'Lifts',
         'text': 'I\'m terrified of lifts....\nI\'m satrting to take steps to avoid them.',
         'date_added': '2018-01-01',
         'upvotes': 44, 'downvotes': 1, 'added_by': 'JoeKadi'},
        {'title': 'Sandwich',
         'text': 'A sandwich walks into a bar...\nThe bartender says "Sorry, we don\'t serve food here!.',
         'date_added': '2018-01-01',
         'upvotes': 11, 'downvotes': 8, 'added_by': 'StuartMcMillan'}
    ]

    adult_jokes = [
        {'title': 'Rubik\'s cube', 'text': 'What do a penis and a Rubik\'s cube have in common?\nThe more you play with it the harder it gets.',
         'date_added': '2018-01-01',
         'upvotes': 5, 'downvotes': 7, 'added_by': 'DavidDamer'},
        {'title': 'Santa',
         'text': 'Why does Santa have such a big sack?\nHe only comes once a year',
         'date_added': '2018-01-01',
         'upvotes': 44, 'downvotes': 1, 'added_by': 'JoeKadi'},
        {'title': 'Lightbulb',
         'text': 'What\'s the difference between a lightbulb and a pregnant woman?\nYou can unscrew a lightbulb.',
         'date_added': '2018-01-01',
         'upvotes': 11, 'downvotes': 8, 'added_by': 'StuartMcMillan'}
    ]

    cats = {
        'Knock Knock':{'jokes': knock_knock_jokes, 'restricted': False, 'num_jokes': len(knock_knock_jokes)},
        'Yo Mama': {'jokes': yo_mama_jokes, 'restricted': False, 'num_jokes': len(yo_mama_jokes)},
        'Chuck Norris':{'jokes': chuck_norris_jokes, 'restricted': False, 'num_jokes': len(chuck_norris_jokes)},
        'Dad Joke':{'jokes': dad_jokes, 'restricted': False, 'num_jokes': len(dad_jokes)},
        'Adult':{'jokes': adult_jokes, 'restricted': True, 'num_jokes': len(adult_jokes)},

    }
    videos = []
    for cat, cat_data in cats.items():
        # c = add_cat(cat)
        # Updated the population script to pass through the specific values for views and likes
        c = add_cat(cat, cat_data["restricted"], cat_data["num_jokes"])
        for joke in cat_data["jokes"]:
            user = User.objects.get(username=joke['added_by'])
            add_joke(category=c, title=joke['title'], text=joke['text'], date_added=joke['date_added'],
                     upvotes=joke['upvotes'], downvotes=joke['downvotes'], added_by=user)


def add_profile(user, date_of_birth, user_bio):
    up = UserProfile.objects.get_or_create(user=user, date_of_birth=date_of_birth)[0]
    up.user_bio = user_bio
    up.save()
    return up


def add_user(name, email, password):
    user = User.objects.get_or_create(username=name, email=email, password=password)[0]
    return user

def add_cat(title, restricted, no_of_jokes):
    cat = Category.objects.get_or_create(title=title, restricted=restricted)[0]
    cat.no_of_jokes = no_of_jokes
    cat.save()
    return cat

def add_joke(title, category, text, date_added, upvotes, downvotes, added_by):
    joke = Joke.objects.get_or_create(title=title, category=category, added_by=added_by)[0]
    joke.joke_text = text
    joke.date_added = date_added
    joke.upvotes = upvotes
    joke.downvotes = downvotes
    joke.save()
    return joke


if __name__ == '__main__':
    print("Starting JokeOverflow population script...")
    populate()