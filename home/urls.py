from . import views

from django.urls import path

from rest_framework_swagger.views import get_swagger_view

# schema for the swagger view
schema_view = get_swagger_view(title='Swagger UI for Xmeme')


urlpatterns = [
    # default route
    path('', views.home, name='home'),

    # route for the swagger ui
    path('swagger-ui/', schema_view),

    # ? api endpoints
    path('memes', views.memes, name='memes'),
    path('memes/<int:id>', views.meme, name='meme'),
]
