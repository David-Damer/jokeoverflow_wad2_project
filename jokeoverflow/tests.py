from django.test import TestCase
from django.core.urlresolvers import reverse
from jokeoverflow.models import Category



class CategoryMethodTests(TestCase):

    # helper method
    
    def add_cat(name, views, likes):
        
        # adds category to dictionary

        c = Category.objects.get_or_create(name=name)[0]
        c.views = views
        c.likes = likes
        c.save()
        return c

    # Create your tests here.

    def test_slug_line_creation(self):

        # tests to check that when we add a category an appropiate slug line is created,
        # i.e 'Category String' --> category-string.

        cat = cat('Random Category String')
        cat.save()
        self.assertEqual(cat.slug, 'random-category-string')

    def test_home_view_with_no_categories(self):

        # test to see if homepage view loads with no categories, appropiate message displayed

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_home_view_with_categories(self):

        # check to make sure that the homepage has categories displayed
        
        add_cat('test',1,1)
        add_cat('temp',1,1)
        add_cat('tmp',1,1)
        add_cat('tmp test temp',1,1)

        response = self.client.get(reverse('index'))
        self.assertEqual(reponse.status_code, 200)
        self.assertContains(response, "tmp test temp")

        num_cats = len(response.context['catergories'])
        self.assertEqual(num_cats, 4)
        

