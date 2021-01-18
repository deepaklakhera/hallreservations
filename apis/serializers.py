from hall.models import Hall,Booking,Professor
from hall.views import check_availability
from rest_framework import serializers

class HallListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hall
        fields=['name','capacity',]

class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=['booking_id','hall','professor','check_in','check_out']

class CreateBookingSerializer(serializers.Serializer):
    capacity=serializers.IntegerField(required=True)
    check_in=serializers.DateTimeField(required=True)
    check_out=serializers.DateTimeField(required=True)

    def create(self,validated_data):

        hall_list=Hall.objects.filter(capacity__gte=validated_data.get('capacity'))
        available_rooms=[]        
        for hall in hall_list:
            
            if check_availability(hall,validated_data['check_in'],validated_data['check_in']):
                available_rooms.append(hall)
        
        if len(available_rooms)>0:
            hall=available_rooms[0]
            
            booking=Booking(
                    hall=hall,                    
                    check_in=validated_data['check_in'],
                    check_out=validated_data['check_in'],
                )
        return booking
