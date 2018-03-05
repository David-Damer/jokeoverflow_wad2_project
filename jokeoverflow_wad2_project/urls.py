"""jokeoverflow_wad2_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from jokeoverflow import views
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

#redirects user to the index page if successful at logging in
class MyRegistrationView(RegistrationView):
    def get_success_ur(self, user):
        return '/home/'

app_name = 'jokeoverflow'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home, name='home'),
    url(r'^about_us/', views.about_us, name='about_us'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^faq/', views.faq, name='faq'),
    url(r'^latest_news/', views.latest_news, name='latest_news'),
    url(r'^top_rated_videos/', views.top_rated_videos, name='top_rated_videos'),
    url(r'^top_rated_jokes/', views.top_rated_jokes, name='top_rated_jokes'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
    url(r'^accounts/register/$',MyRegistrationView.as_view(),name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
