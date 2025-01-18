from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class PropertyDetails(models.Model):
    
    property_name = models.CharField(max_length=200)
    
    PROPERTY_OPTIONS = (
        ("Apartment","Apartment"),
        ("House","House"),
        ("Villa",'Villa'),
        ("RetailSpace","RetailSpace"),
        ("Resort","Resort"),
        ("GuestHouse","GuestHouse"),
        ("PG","PG")
    )
    
    property_type = models.CharField(max_length=200,choices=PROPERTY_OPTIONS,default="Villa")
    
    STATUS_OPTIONS = (
        ("Sale","Sale"),
        ("Rent","Rent"),
        ("Lease","Lease")
    )
    
    property_status = models.CharField(max_length=200,choices=STATUS_OPTIONS,default="Sale")
    
    LOCATION_OPTIONS = (
        ("Thiruvananthapuram","Thiruvananthapuram"),
        ("Kollam","Kollam"),
        ("Pathanamthitta","Pathanamthitta"),
        ("Alappuzha","Alappuzha"),
        ("Kottayam","Kottayam"),
        ("Idukki","Idukki"),
        ("Ernakulam","Ernakulam"),
        ("Thrissur","Thrissur"),
        ("Palakkad","Palakkad"),
        ("Malappuram","Malappuram"),
        ("Kozhikode","Kozhikode"),
        ("Wayanad","Wayanad"),
        ("Kannur","Kannur"),
        ("Kasaragod","Kasaragod")
    )
    
    location = models.CharField(max_length=200,choices=LOCATION_OPTIONS,default="Thiruvananthapuram")
    
    address = models.CharField(max_length=200)
    
    price = models.FloatField()
    
    area = models.FloatField()
    
    no_of_rooms = models.IntegerField()
    
    FURNISHED_OPTIONS = (
        ("Furnished","Furnished"),
        ("Semi-Furnished","Semi-Furnished"),
        ("Unfurnished","Unfurnished")
    )
    
    furnished_status = models.CharField(max_length=200,choices=FURNISHED_OPTIONS,default="Furnished")
    
    owner= models.ForeignKey(User,on_delete=models.CASCADE)
    
    property_image = models.ImageField(upload_to='estateimages',null=True,blank=True)
    
    
    