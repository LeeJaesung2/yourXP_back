from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@api_view(['GET'])
def getUsers(request): #전체 유저 조회
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])
def userDetail(request, user_id): #단일 회원 조회, 수정, 삭제
    user = User.objects.get(pk = user_id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        print(request.data)
        serializer = UserSerializer(user, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response({'message':'sucess', 'code' : 200})

@api_view(['POST'])
def signup_view(request): #회원가입
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request): #로그인
    serializer = UserSerializer(data=request.data)
    username = serializer.initial_data['username']
    password = serializer.initial_data['password']
    user = authenticate(request=request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response(serializer.initial_data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def logout_view(request): #로그아웃
    logout(request)
    return redirect('getUsers')