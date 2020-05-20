from django.shortcuts import render, redirect, HttpResponse
from .forms import Emotion_Typed_Tweet_analyse_form
from .emotion_analysis_code import emotion_analysis_code
from .forms import Emotion_Imported_Tweet_analyse_form
from .tweepy_emotion import Import_tweet_emotion

def emotion_analysis(request):
    return render(request, 'home/emotion.html')

def emotion_analysis_type(request):
    if request.method == 'POST':
        form = Emotion_Typed_Tweet_analyse_form(request.POST)
        analyse = emotion_analysis_code()
        if form.is_valid():
            tweet = form.cleaned_data['emotion_typed_tweet']
            emotion = analyse.predict_emotion(tweet)
            args = {'tweet':tweet, 'emotion':emotion}
            return render(request, 'home/emotion_type_result.html', args)

    else:
        form = Emotion_Typed_Tweet_analyse_form()
        return render(request, 'home/emotion_type.html')

def emotion_analysis_import(request):
    if request.method == 'POST':
        form = Emotion_Imported_Tweet_analyse_form(request.POST)
        tweet_text = Import_tweet_emotion()
        analyse = emotion_analysis_code()

        if form.is_valid():
            handle = form.cleaned_data['emotion_imported_tweet']

            if handle[0]=='#':
                list_of_tweets = tweet_text.get_hashtag(handle)
                list_of_tweets_and_emotions = []
                for i in list_of_tweets:
                    list_of_tweets_and_emotions.append((i,analyse.predict_emotion(i)))
                args = {'list_of_tweets_and_emotions':list_of_tweets_and_emotions, 'handle':handle}
                return render(request, 'home/emotion_import_result_hashtag.html', args)

            list_of_tweets = tweet_text.get_tweets(handle)
            list_of_tweets_and_emotions = []
            if handle[0] != '@':
                handle = str('@' + handle)
            for i in list_of_tweets:
                list_of_tweets_and_emotions.append((i, analyse.predict_emotion(i)))
            args = {'list_of_tweets_and_emotions': list_of_tweets_and_emotions, 'handle': handle}
            return render(request, 'home/emotion_import_result.html', args)

    else:
        form = Emotion_Imported_Tweet_analyse_form()
        return render(request, 'home/emotion_import.html')