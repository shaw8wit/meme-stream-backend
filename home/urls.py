from . import views
from django.urls import path
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),

    # ? api endpoints
    path('memes/', views.memes, name='memes'),
    path('memes/<int:id>', views.meme, name='meme'),
    path('swagger-ui', get_swagger_view(title='XMEME API names:')),
]
