from django.urls import path

from surveysApp import apiviews

app_name = 'surveysApp'
urlpatterns = [
    path('login/', apiviews.login, name='login'),

]
