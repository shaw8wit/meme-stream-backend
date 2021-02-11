from . import views

from django.urls import path

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Swagger UI for Xmeme')


urlpatterns = [
    path('', views.home, name='home'),

    # ? api endpoints
    path('memes', views.memes, name='memes'),
    path('memes/<int:id>', views.meme, name='meme'),
    path('swagger-ui', schema_view)
]
