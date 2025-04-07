from django.db import models
from app.models import User

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=20,null=True,blank=False)
    mobile = models.BigIntegerField(null=True,blank=False,unique=True)
    email = models.EmailField(null=True,blank=False,unique=True,max_length=254)
    usertype = models.CharField(max_length=20)
    cid=models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')
    class Meta:
        db_table = 'customertable'

