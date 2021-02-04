from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # ? api endpoints
    path('memes', views.memes, name='memes'),
    # path('memes/<int:id>', views.memes, name='memes'),
]
