from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    # dest1 = Destination()
    # dest1.name = 'Karachi'
    # dest1.price = 1000
    # dest1.desc = "The city that never sleeps"
    # dest1.img = 'destination_1.jpg'
    # dest1.offer = True

    # dest2 = Destination()
    # dest2.name = "Lahore"
    # dest2.price = 1000
    # dest2.desc = "Lahore Lahore hy"
    # dest2.img = 'destination_2.jpg'
    # dest2.offer = False

    # dest3 = Destination()
    # dest3.name = "Multan"
    # dest3.price = 1000
    # dest3.desc = "Halwa khate jana"
    # dest3.img = 'destination_3.jpg'
    # dest3.offer = False

    
    # dest4 = Destination()
    # dest4.name = "Quetta"
    # dest4.price = 1000
    # dest4.desc = "Quetta Chae p lo"
    # dest4.img = 'destination_4.jpg'
    # dest4.offer = True



    # dest5 = Destination()
    # dest5.name = "Islamabad"
    # dest5.price = 1000
    # dest5.desc = "The destination capital "
    # dest5.img = 'destination_5.jpg'
    # dest5.offer = False

    
    # dest6 = Destination()
    # dest6.name = "Hyderabad"
    # dest6.price = 1000
    # dest6.desc = "Hyderabadi fish"
    # dest6.img = 'destination_6.jpg'
    # dest6.offer = True


    # dests= [dest1,dest2,dest3,dest4,dest5,dest6]



    dests = Destination.objects.all()


    return render(request , 'index.html', {'fin_Dests':dests})
