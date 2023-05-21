from django.db import models
from ckeditor.fields import RichTextField
from user.models import Host,Client
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)

    email = models.EmailField(max_length=200)
    
    message = models.TextField()


    def __str__(self) :
        return self.name




""" 
name , price , rating , review , img , adress , map_X , map_Y , Description , facilities
"""
class Hotel(models.Model):
    name=models.CharField(max_length=200)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    rating=models.DecimalField(blank=True,null=True, max_digits=19, decimal_places=10)
    review=models.IntegerField(blank=True,null=True)
    img=models.ImageField(upload_to='images/hotels')
    adress=models.CharField(max_length=200)
    map_X=models.CharField(max_length=200,blank=True)
    map_Y=models.CharField(max_length=200,blank=True)
    Description=RichTextField()
    facilities=models.TextField(blank=True)
    
    def __str__(self) :
        return self.name


class Rooms(models.Model):
    ROOM_STATUS = ( 
    ("1", "available"), 
    ("2", "not available"),    
    ) 

    ROOM_TYPE = ( 
    ("1", "premium"), 
    ("2", "deluxe"),
    ("3","basic"),    
    ) 

    #type,no_of_rooms,capacity,prices,Hotel
    room_type = models.CharField(max_length=50,choices = ROOM_TYPE)
    capacity = models.IntegerField(default=1)
    price =models.DecimalField(blank=True,null=True,  max_digits=19, decimal_places=10)
    size = models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)
    status = models.CharField(choices =ROOM_STATUS,max_length = 15)
    
    def __str__(self):
        return self.hotel.name


class Reservation(models.Model):

    check_in = models.DateField(auto_now =False)
    check_out = models.DateField()
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    guest = models.ForeignKey(Client, on_delete= models.CASCADE)
    price=models.DecimalField(blank=True,null=True,  max_digits=19, decimal_places=10)
    
    def __str__(self):
        return self.guest.user.userName