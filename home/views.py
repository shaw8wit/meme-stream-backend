from django.shortcuts import render
from django.http import Http404

from .serializers import MemeSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Meme


def index(request):
    return render(request, 'index.html')


@api_view(['GET'])
def home(request):
    api_urls = {
        'Get all Memes': '/memes/',
        'Get details of a Meme': '/memes/<int:id>/',
        'Create a new Meme': '/memes/',
        'Update an existing Meme': '/memes/<int:id>/',
    }
    return Response(api_urls)


@api_view(['GET', 'POST'])
def memes(request):
    try:
        if request.method == 'POST':
            serializer = MemeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'id': serializer.data['id']})
            print(serializer.errors)
            return Response({'error': 'some fields are missing!'})
    except Exception as e:
        print(e)
    memes = Meme.objects.all()
    serializer = MemeSerializer(memes, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PATCH'])
def meme(request, id):
    try:
        meme = Meme.objects.get(id=id)
        if request.method == 'PATCH':
            serializer = MemeSerializer(instance=meme, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = MemeSerializer(meme, many=False)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
