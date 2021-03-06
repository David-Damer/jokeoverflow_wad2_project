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
from jokeoverflow import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'jokeoverflow'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name='home'),
    url(r'^about_us/', views.about_us, name='about_us'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^log_complaint', views.log_complaint, name='log_complaint'),
    url(r'^new_category', views.new_category, name='new_category'),
    url(r'^faq/', views.faq, name='faq'),
    url(r'^latest_news/', views.latest_news, name='latest_news'),
    url(r'^user_profiles/', views.user_profiles, name='user_profiles'),
    url(r'^user_profiles/(?P<username>[\w\-]+)/$', views.user_profiles, name='user_profiles'),
    url(r'^videos/', views.videos, name='videos'),
    url(r'^top_rated_jokes/', views.top_rated_jokes, name='top_rated_jokes'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'register_profile/', views.register_profile, name='register_profile'),
    url(r'^add/$', views.auto_add_video, name='auto_add_video'),
    url(r'^upvote/$', views.upvote, name='upvote'),
    url(r'^downvote/$', views.downvote, name='downvote'),
    url(r'^video_update/$', views.auto_add_video, name='video_update'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_joke/$', views.add_joke, name='add_joke'),
    url(r'^add_comment/$', views.add_comment, name='add_comment'),
    url(r'edit_profile/', views.edit_profile, name='edit_profile'),
    url(r'^video_remove/$', views.video_remove, name='video_remove'),
    url(r'^joke_remove/$', views.joke_remove, name='joke_remove'),
    url(r'^flag/$', views.flag, name='flag'),
    url(r'^delete/', views.delete_user, name='delete_user'),
    url(r'^suggest_joke/$', views.suggest_joke, name='suggest_joke'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

