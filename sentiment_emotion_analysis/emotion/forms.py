from django import forms

class Emotion_Typed_Tweet_analyse_form(forms.Form):
    emotion_typed_tweet = forms.CharField(initial='nothing')

class Emotion_Imported_Tweet_analyse_form(forms.Form):
    emotion_imported_tweet = forms.CharField(initial='nothing')