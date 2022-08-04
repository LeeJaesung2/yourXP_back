from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PostsSerializer
from .models import Posts
# Create your views here.

@api_view(['GET'])
def getPosts(request):
    posts = Posts.objects.all()
    serializer = PostsSerializer(posts, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def createPosts(request):
    serializer = PostsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def updatePosts(request, post_id):
    print(request.data)
    posts = Posts.objects.get(pk = post_id)
    serializer = PostsSerializer(posts, data=request.data, partial = True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletePost(request, post_id):
    post = Posts.objects.get(pk = post_id)
    post.delete()
    return Response({'message':'sucess', 'code' : 200})
