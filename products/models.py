from django.db import models

# Create your models here.
class Product(models.Model):
    brand_name=models.CharField(max_length=250)
    product_name=models.CharField(max_length=250)
    model_name=models.CharField(max_length=250)
    Features=models.TextField()
    category=models.CharField(max_length=100,default="laptop")
    price=models.FloatField()
    stock_in=1
    stock_out=0
    stock_choice=((stock_in,"stock_in"),
            (stock_out,"stock_out"))
    stocks=models.IntegerField(choices=stock_choice,default=0)
    image=models.ImageField(upload_to="media")
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.product_name
    class Meta:
        db_table = 'productstable'

