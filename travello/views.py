from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = "Karachi"
    dest1.price = 1000
    dest1.desc = "The city that never sleeps"

    return render(request, 'index.html',{'dest':dest1})
