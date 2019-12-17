from django.db import models

# Create your models here.
class Destination:
    price : int
    desc : str
    name : str
    id : int
    image = str
    offer  = bool
