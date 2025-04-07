from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    usertype=models.CharField(max_length=50)
    is_approved = models.BooleanField(default=False)

    class Meta:
        db_table = 'adminstable'




