from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    
    dest1 = Destination() 
    dest1.name = 'Ethiopia'   
    dest1.desc = 'The Land of Origin'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = False
    
    dest2 = Destination() 
    dest2.name = 'Addis Ababa'   
    dest2.desc = 'The City where I live in'
    dest2.img = 'destination_2.jpg'
    dest2.price = 550
    dest2.offer = True
    
    dest3 = Destination() 
    dest3.name = 'Hawassa'   
    dest3.desc = 'The City where my soupes live'
    dest3.img = 'destination_3.jpg'
    dest3.price = 400
    dest3.offer = True
    
    dests = [dest1,dest2, dest3]
    
    return render(request, "index.html", {'dests': dests})