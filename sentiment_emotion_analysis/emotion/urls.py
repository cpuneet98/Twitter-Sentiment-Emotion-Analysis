from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'emotion'

urlpatterns = [
    url(r'^$', views.emotion_analysis, name="emotion_anaylsis"),
    url(r'^type/$', views.emotion_analysis_type, name="emotion_analysis_type"),
    url(r'^import/$', views.emotion_analysis_import, name="emotion_analysis_import"),
]