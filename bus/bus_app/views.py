from django.shortcuts import render
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer, BusSerializer
from .models import *


# Create your views here.

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token,created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {'token': token.key,
                 'user_id': user.id},
                status=status.HTTP_200_OK
            )
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class BusCreateView(ListAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class BusDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class BookingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        seat_id = request.data.get('seat')
        try:
            seat = Seat.objects.get(id=seat_id)
            if seat.is_booked:
                return Response({"error": "seat is already booked"}, status=status.HTTP_400_BAD_REQUEST)
            seat.is_booked = True
            seat.save()
            bookings = Booking.objects.create(
                user=request.user,
                bus=seat.bus,
                seat=seat
            )
            serializer = BusSerializer(bookings)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Seat.DoesNotExist:
            return Response({'error': "Invalid Seat id"}, status=status.HTTP_400_BAD_REQUEST)


class UserBookingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        if request.user.id != user_id:
            return Response({'error': 'unauthorised'}, status=status.HTTP_401_UNAUTHORIZED)
        bookings = Booking.objects.filter(id=user_id)
        serializer = BusSerializer(bookings, many=True)
        return Response(serializer.data)
