from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime
import uuid
# Create your models here.
User=settings.AUTH_USER_MODEL

class Professor(models.Model):    
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Hall(models.Model):
    # room_size=(
    #     ('Hall A','50'),
    #     ('Hall B','100'),
    #     ('Hall C','200'),
    #     ('Hall D','350'),
    #     ('Hall E','500'),
    #     ('Hall F','1000'),
    # )
    # capacity=models.CharField(max_length=7,choices=room_size)
    name=models.CharField(max_length=50)
    capacity=models.PositiveIntegerField()
    # is_booked=models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

class Booking(models.Model):
    
    booking_id=models.CharField(max_length=50, null=True, blank=True, unique=True, default=uuid.uuid4)
    hall=models.ForeignKey(Hall,on_delete=models.CASCADE)
    professor=models.ForeignKey(Professor,on_delete=models.CASCADE)
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()

    def __str__(self):
        return f'Booking for {str(self.hall)} -{self.booking_id} '













@receiver(post_save,sender=User)
def post_save_user_create_professor(sender,instance,created,*args,**kwargs):
    if created:
        Professor.objects.create(user=instance)
    
