from django.db import models
from app.models import User


# Create your models here.
# approved seller
class Seller(models.Model):
    sname = models.CharField(max_length=20,null=True,blank=False)
    smobile = models.BigIntegerField(null=True,blank=False,unique=True)
    semail = models.EmailField(null=True,blank=False,unique=True,max_length=254)
    slocation = models.CharField(max_length=20,null=True,blank=False)
    usertype = models.CharField(max_length=20)
    sid=models.ForeignKey(User,on_delete=models.CASCADE,related_name='seller_profile')
    class Meta:
        db_table = 'sellersrtable'
    def __str__(self):
        return self.sname

# pending seller
class Approve_Seller(models.Model):
    sname = models.CharField(max_length=20,null=True,blank=False)
    smobile = models.BigIntegerField(null=True,blank=False,unique=True)
    semail = models.EmailField(null=True,blank=False,unique=True,max_length=254)
    slocation = models.CharField(max_length=20,null=True,blank=False)
    password=models.CharField(max_length=20)
   
    class Meta:
        db_table = 'Pending_seller'
    def __str__(self):
        return self.sname