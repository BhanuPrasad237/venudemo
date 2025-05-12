from django.shortcuts import render
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer,BusSerializer
from .models import *
# Create your views here.

class UserRegisterView(APIView):
    def post(self):
        serializer=UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'token':token.key},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username,password=password)
        if user:
            token,created=Token.objects.create(user=user)
            return Response(
                {'token':token.key,
                 'user_id':user.id},
                status=status.HTTP_200_OK
            )
        return Response({'error':'Invalid Credentials'},status=status.HTTP_401_UNAUTHORIZED)

class BusCreateView(ListAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

class BusDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
