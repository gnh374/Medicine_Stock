from django.urls import path
from main.views import show_main

app_name = 'main'

#url untuk app main
urlpatterns = [
    #url homepage app main
    path('', show_main, name='show_main'),
]