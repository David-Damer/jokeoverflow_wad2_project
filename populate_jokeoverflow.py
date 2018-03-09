import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jokeoverflow_wad2_project.settings')

import django

django.setup()

from jokeoverflow.models import UserProfile, Comment, Joke, Video, Category
from django.contrib.auth.models import User


def populate():
    # Create users
    users = [
        {'name': 'EricCarpenter', 'email': 'eric@thepub.com', 'password': 'p@ssw0rd1',
         'date_of_birth': '1965-05-07', 'user_bio': 'I\'m a retired carpenter, my pals in the pub say I\'m  hilarious '
                                                    'so I thought I\'d give this site a wee go.'},
        {'name': 'WeeCraig', 'email': 'w33craig@thehoose.com', 'password': 'p@ssw0rd2',
         'date_of_birth': '1992-12-10',
         'user_bio': 'I\'m serious about comedy, but nothing too smutty will get past me!\n '
                     'I\'m a merchant banker by day and joke moderator by night. '},
        {'name': 'SammyTheMan', 'email': 'sammy@thebbc.co.uk', 'password': 'p@ssw0rd3',
         'date_of_birth': '1994-02-16', 'user_bio': 'I write jokes for the BBC and I come here for inspiration.'},
        {'name': 'PatriciaWorker', 'email': 'fatpat@theoffice.com', 'password': 'p@ssw0rd4',
         'date_of_birth': '1994-04-06', 'user_bio': 'I\'m an office worker for a construction company.\n'
                                                    'The only light relief I get is at lunchtime when I\'m '
                                                    'browsing joke overflow.'},
        {'name': 'JimmyJokington', 'email': 'jj@home.com', 'password': 'p@ssw0rd5',
         'date_of_birth': '2002-04-06', 'user_bio': 'I like to try these jokes on the girls at school in the hope that'
                                                    ' one will go out with me.'},
    ]

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
         'upvotes': 5, 'downvotes': 7, 'added_by': 'PatriciaWorker'},
        {'title': 'Canoe Joke',
         'text': 'Knock knock.\nWho\'s there?\nCanoe.\nCanoe who?\nCanoe help with my homework?.',
         'date_added': '2018-01-08',
         'upvotes': 10, 'downvotes': 2, 'added_by': 'SammyTheMan'},
        {'title': 'Iva Joke',
         'text': 'Knock knock.\nWho\'s there?\nIva.\nIva who?\nIva sore hand from knocking.',
         'date_added': '2017-07-08',
         'upvotes': 12, 'downvotes': 9, 'added_by': 'WeeCraig'},
        {'title': 'Isabell',
         'text': 'Knock knock.\nWho\'s there?\nIsabell.\nIsabell who?\nIsabell not working?',
         'date_added': '2017-09-21',
         'upvotes': 12, 'downvotes': 9, 'added_by': 'JimmyJokington'},
        {'title': 'Tank',
         'text': 'Knock knock.\nWho\'s there?\nTank.\nTank who?\nYou\'re welcome.',
         'date_added': '2017-09-18',
         'upvotes': 12, 'downvotes': 9, 'added_by': 'WeeCraig'},
    ]

    yo_mama_jokes = [
        {'title': 'Fat mama joke', 'text': 'Yo mama so fat, she doesn\'t need the internet; she already world wide!',
         'date_added': '2017-09-18',
         'upvotes': 5, 'downvotes': 7, 'added_by': 'EricCarpenter'},
        {'title': 'Hockey Joke',
         'text': 'Yo mama is like a hockey player, she only showers after three periods.',
         'date_added': '2017-11-14',
         'upvotes': 3, 'downvotes': 5, 'added_by': 'SammyTheMan'},
        {'title': 'Ugly Joke',
         'text': 'Yo mama so ugly, she tried to enter an ugliness competition and they said "No professionals".',
         'date_added': '2017-10-10',
         'upvotes': 9, 'downvotes': 5, 'added_by': 'WeeCraig'},
        {'title': 'Disneyland',
         'text': 'Yo mama so stupid, when yous were going to disneyland the sign said "disneyland left" '
                 'so she went home again',
         'date_added': '2018-01-01',
         'upvotes': 12, 'downvotes': 9, 'added_by': 'PatriciaWorker'},
        {'title': 'Ruler',
         'text': 'Yo mama so stupid she took a ruler to bed to see how long she slept.',
         'date_added': '2017-10-10',
         'upvotes': 12, 'downvotes': 9, 'added_by': 'WeeCraig'},
    ]

    chuck_norris_jokes = [
        {'title': 'Death', 'text': 'Death once had a near Chuck experience',
         'date_added': '2017-06-05',
         'upvotes': 5, 'downvotes': 7, 'added_by': 'EricCarpenter'},
        {'title': 'Street',
         'text': 'There used to be a street named after Chuck Norris. They had to change the name because nobody '
                 'crosses Chuck Norris and lives.',
         'date_added': '2017-06-05',
         'upvotes': 44, 'downvotes': 1, 'added_by': 'PatriciaWorker'},
        {'title': 'Guns',
         'text': 'Guns carry Chuck Norris for protection.',
         'date_added': '2018-03-05',
         'upvotes': 11, 'downvotes': 8, 'added_by': 'WeeCraig'},
        {'title': 'Condoms',
         'text': 'Chuck Norris uses ribbed condoms inside out so that he gets the pleasure.',
         'date_added': '2018-03-05',
         'upvotes': 12, 'downvotes': 9, 'added_by': 'JimmyJokington'},
        {'title': 'Horses',
         'text': 'Chuck Norris isn\'t hung like a horse, horses are hung like Chuck Norris.',
         'date_added': '2017-09-05',
         'upvotes': 12, 'downvotes': 9, 'added_by': 'WeeCraig'},
    ]

    dad_jokes = [
        {'title': 'Hungry', 'text': 'Dad, I\'m hungry...\nHi hungry I\'m dad',
         'date_added': '2017-09-05',
         'upvotes': 5, 'downvotes': 7, 'added_by': 'EricCarpenter'},
        {'title': 'Lifts',
         'text': 'I\'m terrified of lifts....\nI\'m starting to take steps to avoid them.',
         'date_added': '2017-12-07',
         'upvotes': 44, 'downvotes': 1, 'added_by': 'PatriciaWorker'},
        {'title': 'Sandwich',
         'text': 'A sandwich walks into a bar...\nThe bartender says "Sorry, we don\'t serve food here!.',
         'date_added': '2017-10-03',
         'upvotes': 11, 'downvotes': 8, 'added_by': 'WeeCraig'},
        {'title': 'Dentist',
         'text': 'What time do you go to the dentist?\nAt tooth-hurty!.',
         'date_added': '2017-10-03',
         'upvotes': 12, 'downvotes': 9, 'added_by': 'SammyTheMan'},
        {'title': 'Peanuts',
         'text': 'Two peanuts were walking down a street.\nOne was a salted.',
         'date_added': '2018-02-03',
         'upvotes': 12, 'downvotes': 9, 'added_by': 'SammyTheMan'},
        {'title': 'Calendar',
         'text': 'I had a job at the calendar factory but I got the sack for taking days off.',
         'date_added': '2018-02-03',
         'upvotes': 12, 'downvotes': 9, 'added_by': 'WeeCraig'},
    ]

    adult_jokes = [
        {'title': 'Rubik\'s cube',
         'text': 'What do a penis and a Rubik\'s cube have in common?\nThe more you play with it the harder it gets.',
         'date_added': '2017-02-28',
         'upvotes': 5, 'downvotes': 7, 'added_by': 'EricCarpenter'},
        {'title': 'Santa',
         'text': 'Why does Santa have such a big sack?\nHe only comes once a year',
         'date_added': '2017-12-25',
         'upvotes': 44, 'downvotes': 1, 'added_by': 'PatriciaWorker'},
        {'title': 'Lightbulb',
         'text': 'What\'s the difference between a lightbulb and a pregnant woman?\nYou can unscrew a lightbulb.',
         'date_added': '2017-07-25',
         'upvotes': 11, 'downvotes': 8, 'added_by': 'WeeCraig'},
        {'title': 'Wife',
         'text': 'What\' the difference between your wife and your job?\nAfter five years your job will still suck.',
         'date_added': '2017-08-22',
         'upvotes': 12, 'downvotes': 9, 'added_by': 'WeeCraig'},
        {'title': 'Oral',
         'text': 'What\'s the difference between anal and oral sex?\nOral sex makes your day.\nAnal sex makes your hole weak.',
         'date_added': '2017-08-22',
         'upvotes': 12, 'downvotes': 9, 'added_by': 'WeeCraig'},
    ]

    cats = {
        'Knock Knock': {'jokes': knock_knock_jokes, 'restricted': False, 'num_jokes': len(knock_knock_jokes)},
        'Yo Mama': {'jokes': yo_mama_jokes, 'restricted': False, 'num_jokes': len(yo_mama_jokes)},
        'Chuck Norris': {'jokes': chuck_norris_jokes, 'restricted': False, 'num_jokes': len(chuck_norris_jokes)},
        'Dad Joke': {'jokes': dad_jokes, 'restricted': False, 'num_jokes': len(dad_jokes)},
        'Adult': {'jokes': adult_jokes, 'restricted': True, 'num_jokes': len(adult_jokes)},

    }
    videos = [
        {'title': 'Compilation', 'url': 'https://www.youtube.com/watch?v=DODLEX4zzLQ', 'added_by': 'WeeCraig',
         'date_added': '2017-08-08', 'upvotes': 7, 'downvotes': 22
         },
        {'title': 'Laugh til you Fart', 'url': 'https://www.youtube.com/watch?v=bXZEP6OwKBQ',
         'added_by': 'PatriciaWorker',
         'date_added': '2017-09-12', 'upvotes': 8, 'downvotes': 9
         },
        {'title': 'Auditions', 'url': 'https://www.youtube.com/watch?v=2uxtfgx5S2s', 'added_by': 'SammyTheMan',
         'date_added': '2018-02-12', 'upvotes': 22, 'downvotes': 7
         },
        {'title': 'Fails', 'url': 'https://www.youtube.com/watch?v=iqV9aAqBhqA', 'added_by': 'EricCarpenter',
         'date_added': '2018-10-12', 'upvotes': 41, 'downvotes': 144
         },
        {'title': 'Dogs', 'url': 'https://www.youtube.com/watch?v=aEzZLXBH3rU', 'added_by': 'EricCarpenter',
         'date_added': '2018-10-09', 'upvotes': 12, 'downvotes': 8
         }

    ]
    comments = [
        {'text': 'This is hilarious, tell me another!', 'joke': 'Dr who joke', 'added_by': 'WeeCraig',
         'date_added': '2018-02-02'},
        {'text': 'Hahaha rofl.', 'joke': 'Hungry', 'added_by': 'PatriciaWorker',
         'date_added': '2018-01-18'},
        {'text': 'This is so sad!', 'joke': 'Sandwich', 'added_by': 'SammyTheMan',
         'date_added': '2018-01-22'},
        {'text': 'Good joke!', 'joke': 'Street', 'added_by': 'PatriciaWorker',
         'date_added': '2018-01-07'},
        {'text': 'I don\'t get it!', 'joke': 'Rubik\'s cube', 'added_by': 'EricCarpenter',
         'date_added': '2018-02-25'},
        {'text': 'I pure love Chuck Norris jokes!!!', 'joke': 'Death', 'added_by': 'SammyTheMan',
         'date_added': '2018-02-25'},
        {'text': 'OMG ', 'joke': 'Ugly Joke', 'added_by': 'EricCarpenter',
         'date_added': '2018-03-04'},
        {'text': 'Well, it is true.', 'joke': 'Lightbulb', 'added_by': 'PatriciaWorker',
         'date_added': '2018-01-04'},
        {'text': 'You\'ve ruined xmas for me!', 'joke': 'Santa', 'added_by': 'SammyTheMan',
         'date_added': '2018-01-12'},
        {'text': 'Really come on, try harder.', 'joke': 'Lifts', 'added_by': 'WeeCraig',
         'date_added': '2017-12-30'},
        {'text': 'I feel sick after reading this.', 'joke': 'Hockey Joke', 'added_by': 'WeeCraig',
         'date_added': '2017-12-31'},
        {'text': 'Gold, pure gold.', 'joke': 'Fat mama joke', 'added_by': 'PatriciaWorker',
         'date_added': '2018-02-17'},
        {'text': 'I\'ve a sore hand. Get it?', 'joke': 'Iva Joke', 'added_by': 'EricCarpenter',
         'date_added': '2018-02-14'},
        {'text': 'Groan', 'joke': 'Canoe Joke', 'added_by': 'SammyTheMan',
         'date_added': '2018-02-16'},
        {'text': 'Yeeeeeee haaaa!', 'joke': 'Guns', 'added_by': 'EricCarpenter',
         'date_added': '2018-02-04'},
        {'text': 'This is older than me.', 'joke': 'Dr who joke', 'added_by': 'SammyTheMan',
         'date_added': '2018-02-02'},

    ]
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["restricted"], cat_data["num_jokes"])
        for joke in cat_data["jokes"]:
            user = User.objects.get(username=joke['added_by'])
            add_joke(category=c, title=joke['title'], text=joke['text'], date_added=joke['date_added'],
                     upvotes=joke['upvotes'], downvotes=joke['downvotes'], added_by=user)

    for video in videos:
        usr = User.objects.get(username=video['added_by'])
        add_video(title=video['title'], url=video['url'], added_by=usr, date_added=video['date_added'],
                  upvotes=video['upvotes'], downvotes=video['downvotes'])

    for comment in comments:
        usr = User.objects.get(username=comment['added_by'])
        joke = Joke.objects.get(title=comment['joke'])
        add_comment(comment_text=comment['text'], added_by=usr, joke=joke, date_added=comment['date_added'])


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
    joke.rating = upvotes - downvotes
    joke.save()
    return joke


def add_video(title, url, date_added, added_by, upvotes, downvotes):
    vid = Video.objects.get_or_create(title=title, added_by=added_by)[0]
    vid.url = url
    vid.date_added = date_added
    vid.upvotes = upvotes
    vid.downvotes = downvotes
    vid.rating = upvotes - downvotes
    vid.embed_code ='https://www.youtube.com/embed/' + url.split('=')[-1]
    vid.save()
    return vid


def add_comment(comment_text, added_by, date_added, joke):
    comment = Comment.objects.get_or_create(made_by=added_by, joke=joke)[0]
    comment.comment_text = comment_text
    comment.date_added = date_added
    comment.save()
    return comment


if __name__ == '__main__':
    print("Starting JokeOverflow population script...")
    populate()
