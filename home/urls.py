from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # ? api endpoints
    path('home/', views.home, name='home'),
    path('memes/', views.memes, name='memes'),
    path('memes/<int:id>', views.meme, name='meme')
    # path('memes/<int:id>', views.memes, name='memes'),
]
