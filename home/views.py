from .serializers import MemeSerializer, MemesSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Meme


@api_view(['GET'])
def home(request):
    """
    The default route allowing only get request
    """

    # details about the backend
    api_urls = {
        'endpoints': {
            '/memes': {
                'GET': 'returns an array of all memes in database',
                'POST': {
                    'description': 'adds memes to database',
                    'parameteres': {
                        'name': 'name of the meme maker, required, not-editable',
                        'caption': 'captin for the meme, required, can be edited later',
                        'url': 'url of the meme image, required, can be edited later',
                    },
                },
            },
            '/memes/<id>': {
                'GET': 'returns the data of the meme with id = <id>',
                'POST': {
                    'description': 'edits meme with id = <id> in database',
                    'parameteres': {
                        'caption': 'captin for the meme, optional, cant be set to empty',
                        'url': 'url of the meme image, optional, cant be set to empty',
                    },
                },
            },
        },
    }
    return Response(api_urls)


@api_view(['GET', 'POST'])
def memes(request):
    """
    The /memes route allowing GET and POST request.

    GET returns all the memes in the database.

    POST a request to add memes to database.
    """
    try:

        # check if method is post else goes to get part
        if request.method == 'POST':

            # using the model serializer to get and check the request data
            serializer = MemesSerializer(data=request.data)

            # proceed only if the data sent is valid according to the serializer
            if serializer.is_valid():
                name = serializer.validated_data['name']
                url = serializer.validated_data['url']
                caption = serializer.validated_data['caption']

                # dont let any of the fields be empty
                if '' not in [name, url, caption]:

                    # check if the meme already exists
                    existingMeme = Meme.objects.filter(
                        name=name, caption=caption, url=url)

                    # create meme if it doesn't already exist and return 201
                    if not existingMeme:
                        serializer.save()
                        return Response({'id': f"{serializer.data['id']}"}, status=status.HTTP_201_CREATED)

                    # return conflict 409 if meme already exists
                    return Response(status=status.HTTP_409_CONFLICT)

            # return bad request 400 if any of the fields are empty
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # if its a GET request the get all memes from database
        memes = reversed(Meme.objects.all().order_by('-id')[:100])
        serializer = MemesSerializer(memes, many=True)

        # return the serialized data with 200 status code
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:

        # return server error if something goes wrong or unexpected happens
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PATCH'])
def meme(request, id):
    """
    The /memes/{id} route allowing GET and PATCH request.

    GET returns details of the meme with the given id.

    PATCH edits the caption and url of the meme with the given id.
    """
    try:
        try:

            # get the meme with the specified [id]
            meme = Meme.objects.get(id=id)

            # check if a PATCH request is sent
            if request.method == 'PATCH':

                # serialize the data sent and check for its validity
                serializer = MemeSerializer(instance=meme, data=request.data)
                if serializer.is_valid():

                    # if name is provided then change it to original
                    # as the name cant be changed once set
                    if 'name' in serializer.validated_data:
                        serializer.validated_data['name'] = meme.name

                    # if everything goes well then save the meme and return 204
                    serializer.save()
                    return Response(status=status.HTTP_204_NO_CONTENT)

                # if you try to set a field to empty return bad request
                return Response(status=status.HTTP_400_BAD_REQUEST)

            # if the request is GET then return the meme with 200 status code
            serializer = MemesSerializer(meme, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:

            # if this throws an error while getting the meme,
            # it means that meme with the [id] doesnt exits so return 404
            return Response(status=status.HTTP_404_NOT_FOUND)
    except:

        # return server error if something goes wrong or unexpected happens
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
