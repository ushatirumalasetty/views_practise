from django.shortcuts import render

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *

class CreateSnippetRequest:
    def __init__(self, code, title=''):
        self.title = title
        self.code = code


class CreateSnippetRequestSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_blank=True,
                                  max_length=100)
    code = serializers.CharField()

    def create(self, validated_data):
        return CreateSnippetRequest(**validated_data)


class CreateSnippetResponseClass:
    def __init__(self, id, title, code):
        self.id = id
        self.title = title
        self.code = code


class CreateSnippetResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(required=False, allow_blank=True,
                                  max_length=100)
    code = serializers.CharField()

    def create(self, validated_data):
        return CreateSnippetResponseClass(**validated_data)

@api_view(['POST'])
def create_snippet(request):
    """
    Create a new snippet.
    """
    
    serializer = CreateSnippetRequestSerializer(data=request.data)
    if serializer.is_valid():
        request_obj = serializer.save()
        dummy_snippet_object = CreateSnippetResponseClass(
            id=1,
            title="usha",
            code="print(123)"
        )
        new_snippet_obj = create_snippet_in_db(request_obj.title, request_obj.code)
        response_serializer = CreateSnippetResponseSerializer(new_snippet_obj)
        return Response(response_serializer.data)
        
@api_view(['GET'])
def get_list_of_snippets(request):
    snippet_objs = Snippet.objects.all().order_by("-id")
    response_serializer = CreateSnippetResponseSerializer(snippet_objs, many=True)
    return Response(response_serializer.data)
