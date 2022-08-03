from functools import partial
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PostSerializer
from .serializer import ReviewSerializer
from .models import Post
from .models import Review
from sellXP import serializer

# Create your views here.
@api_view(['GET'])
def getReviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getReviewById(request, review_id):
    review = Review.objects.get(pk = review_id)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

@api_view(['POST'])
def createReview(request, post_id):
    post = Post.objects.get(pk = post_id)
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def updateReview(request, review_id):
    print(request.data)
    review = Review.objects.get(pk = review_id)
    serializer = ReviewSerializer(review, data=request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteReview(request, review_id):
    review = Review.objects.get(pk = review_id)
    review.delete()
    return Response({'message':'sucess', 'code' : 200})