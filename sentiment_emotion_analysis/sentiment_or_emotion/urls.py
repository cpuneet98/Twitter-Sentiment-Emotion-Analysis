from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'sentiment_or_emotion'

urlpatterns = [
    url(r'^$', views.choose_sentiment_or_emotion, name="choose_sentiment_or_emotion"),
]