from django.shortcuts import render
from hall.models import Hall,Professor,Booking
from rest_framework.response import Response
from .serializers import HallListSerializer,BookingListSerializer,CreateBookingSerializer
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET','POST'])
def listHalls(request,*args,**kwargs):
    queryset=Hall.objects.all()
    if request.method=='GET':        
        serializer=HallListSerializer(queryset,many=True)
        return Response(serializer.data,status=200)

    elif request.method=='POST':

        serializer=HallListSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=404)



@api_view(['GET',])
def BookingHalls(request,*args,**kwargs):
    queryset=Booking.objects.all()
    serializer=BookingListSerializer(queryset,many=True)

    return Response(serializer.data,status=200)

@api_view(['POST',])
def createBooking(request,*args,**kwargs):
    if request.method=='POST':
        serializer=CreateBookingSerializer(data=request.data)
        professor=Professor.objects.get(user=request.user)
        
        if serializer.is_valid(raise_exception=True):
            
            serializer.save(professor=professor)
        return Response("Booking Done successfully")
