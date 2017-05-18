from django.conf.urls import url
from . import views

app_name = 'homepage'

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^tweet', views.post_tweet, name='tweet')
]
