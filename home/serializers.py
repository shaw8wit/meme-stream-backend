from rest_framework import serializers
from .models import Meme


class MemeSerializer(serializers.ModelSerializer):
    """
    Serializer where the fields are optional.
    Used in PATCH request.
    """
    class Meta:
        model = Meme
        fields = '__all__'
        extra_kwargs = {"name": {"required": False, "allow_null": True},
                        "url": {"required": False, "allow_null": True},
                        "caption": {"required": False, "allow_null": True}}


class MemesSerializer(serializers.ModelSerializer):
    """
    Serializer where the fields are required.
    Used in POST request.
    """
    class Meta:
        model = Meme
        fields = '__all__'
