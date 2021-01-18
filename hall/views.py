from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,FormView

from django.core.serializers.json import DjangoJSONEncoder
from .models import Professor,Hall,Booking
from .forms import AvailabilityForm
import json

# Create your views here.
class HallListView(ListView):
    model=Hall
    template_name='hall/listHall.html'

class BookingListView(ListView):
    model=Booking
    template_name='hall/listBooking.html'

class BookingView(FormView):
    form_class=AvailabilityForm
    template_name='hall/availabilityForm.html'
    
    
    def form_valid(self,form):
        
        data=form.cleaned_data

        hall_list=Hall.objects.filter(capacity__gte=data.get('capacity'))        
        available_rooms=[]
        
        for hall in hall_list:
            
            if check_availability(hall,data['check_in'],data['check_out']):
                available_rooms.append(hall)

        
        if len(available_rooms)>0:
            self.request.session['check_in']=json.dumps(data['check_in'],cls=DjangoJSONEncoder)
            self.request.session['check_out']=json.dumps(data['check_out'],cls=DjangoJSONEncoder)
           
            return render(self.request,'hall/available_room.html',{'available_rooms':available_rooms})
           
        else:
            return HttpResponse("No hall available for selected Date/time")

def confirm_booking(request,id,*args,**kwargs):
    try:
        check_in=json.loads(request.session['check_in'])
        check_out=json.loads(request.session['check_out'])
    except:
        return HttpResponse("Invalid selection")

    professor=Professor.objects.get(user=request.user)

    if check_in !=None and check_out != None:

        try:
            hall=get_object_or_404(Hall,pk=id)
            print(Hall,"--------------------",professor,check_in,check_out)
            booking=Booking(
                    hall=hall,
                    professor=professor,
                    check_in=check_in,
                    check_out=check_out,
                )
            booking.save()
            request.session['check_in']=None
            request.session['check_out']=None
            context={
                "hallname":hall.name,
                "check_in":check_in,
                "check_out":check_out,
            }
            return render (request,'hall/confirmbooked.html',context)
            
        except Exception as e:
            return HttpResponse("An error occured")
    else:
        return HttpResponse("Invalid selection")

    print()

    return HttpResponse("Booking")

def check_availability(hall,check_in,check_out):
    hall_booking_list=Booking.objects.filter(hall=hall)
    avail_list=[]
    for hall in hall_booking_list:
        if check_out<hall.check_in or check_in>hall.check_out:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)