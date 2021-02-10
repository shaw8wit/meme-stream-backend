import coreapi

from django.shortcuts import render

from .serializers import MemeSerializer, MemesSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.schemas import AutoSchema

from .models import Meme


class MemesSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'patch']:
            extra_fields = [
                coreapi.Field('name'),
                coreapi.Field('caption'),
                coreapi.Field('url')
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


schema = MemesSchema()


@api_view(['GET'])
def home(request):
    api_urls = {
        'Get all Memes': '/memes',
        'Get details of a Meme': '/memes/<int:id>',
        'Create a new Meme': '/memes',
        'Update an existing Meme': '/memes/<int:id>',
    }
    return Response(api_urls)


@api_view(['GET', 'POST'])
def memes(request):
    try:
        if request.method == 'POST':
            serializer = MemesSerializer(data=request.data)
            if serializer.is_valid():
                name = serializer.validated_data['name']
                url = serializer.validated_data['url']
                caption = serializer.validated_data['caption']
                if '' not in [name, url, caption]:
                    existingMeme = Meme.objects.filter(
                        name=name, caption=caption, url=url)
                    if not existingMeme:
                        serializer.save()
                        return Response({'id': f"{serializer.data['id']}"}, status=status.HTTP_201_CREATED)
                    else:
                        return Response(status=status.HTTP_409_CONFLICT)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        memes = reversed(Meme.objects.all().order_by('-id')[:100])
        serializer = MemesSerializer(memes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PATCH'])
def meme(request, id):
    try:
        try:
            meme = Meme.objects.get(id=id)
            if request.method == 'PATCH':
                serializer = MemeSerializer(instance=meme, data=request.data)
                if serializer.is_valid():
                    if 'name' in serializer.validated_data:
                        serializer.validated_data['name'] = meme.name
                    serializer.save()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            serializer = MemesSerializer(meme, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
