from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from django.utils import timezone
from django.contrib.auth.models import User
from jokeoverflow.forms import *
from jokeoverflow.models import *


class GenericTests(TestCase):

    def test_working(self):

        # test to check if tests are working via simple addition

        self.assertEqual(1 + 1, 2)

    def test_static_files(self):

        # test if static media is used correctly. expepcted output = not NONE

        result = finders.find('images/logo.png')
        self.assertIsNotNone(result)

    def test_home_response(self):

        # tests where the homepage url responds

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
    def test_home_template(self):

        # test to check if homepage using correct template

        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'jokeoverflow/base2.html')

    def test_population_script(self):

        # tests to check if population script runs
        
        try:
            from population_script import populate_jokeoverflow
            populate_jokeoverflow()
        except ImportError:
            print('population_script does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function')

    def test_valid_user(self):

        # tests userform with valid data
        
        form = UserForm(data={'username': "testuser", 'email': "test@test.com", 'password': "123abc123"})
        self.assertTrue(form.is_valid())

    def test_invalid_user(self):

        # tests userform with invalid data
        
        form = UserForm(data={'username': "testuser", 'email': "testtest.com", 'password': "n/a"})
        self.assertFalse(form.is_valid())

    def test_valid_category(self):

        # tests if category model works
        
        category = Category.objects.create(title="test category", restricted=False, no_of_jokes=1, slug="test_category")
        self.assertTrue(isinstance(category, Category))

    def test_valid_joke(self):

        # test if joke creation with category and user
        
        user = User.objects.create(username="testuser", password="testpass")
        category = Category.objects.create(title="test category", restricted=False, no_of_jokes=1, slug="test_category")
        joke = Joke.objects.create(title="title", joke_text="joketext", date_added=timezone.now(), upvotes=1, downvotes=1, flagged=False, category=category, added_by=user, rating=1, slug="title") 
        self.assertTrue(isinstance(joke, Joke))
