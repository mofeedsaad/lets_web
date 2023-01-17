from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):

    user =models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    

class product(models.Model):
     CATEGORY=(
         ('T-shirt','T-shirt'),
         ('pants','pants'),
         ('shoes','shoes'),
     )

     name = models.CharField(max_length=200,null=True)
     catagory = models.CharField(max_length=200,null=True,choices=CATEGORY)
     description = models.CharField(max_length=200,null=True)
     date_created = models.DateTimeField(auto_now_add=True,null=True)
     image = models.ImageField(null=True,blank=True)

     def __str__(self):
        return self.name

     @property
     def imageURL(self):
        try  :
            url=self.image.url
        except :
            url= ''
        return url

class Order(models.Model):
    

     Customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
     product=models.ForeignKey(product,null=True,on_delete=models.SET_NULL)

    
     date_created = models.DateTimeField(auto_now_add=True,null=True)
    

