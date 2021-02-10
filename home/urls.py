from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),

    # ? api endpoints
    path('memes', views.memes, name='memes'),
    path('memes/<int:id>', views.meme, name='meme')
]
