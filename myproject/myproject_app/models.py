from django.db import models

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=100)
    sub_title= models.CharField(max_length=100)
    description =  models.CharField(max_length=500)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to= 'photos', null= True, blank= True)
    
    
    def __str__(self):
        return self.title

# class Services(models.Model):
#     service_title = models.CharField(max_length=100)
#     sub_title= models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#     price = models.DecimalField( max_digits=5, decimal_places=2)
    
    
#     def __str__(self):
#         return self.service_title



class Order(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=7)
    cvv = models.CharField(max_length=3)
    
    def __str__(self):
        return self.full_name
