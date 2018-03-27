from jokeoverflow.models import Joke
import django_filters

class JokeFilter(django_filters.FilterSet):
    class Meta:
        model = Joke
        fields = ['title', 'joke_text', 'date_added', 'upvotes',
                  'downvotes', 'flagged', 'category', 'added_by',
                  'rating', 'slug']
