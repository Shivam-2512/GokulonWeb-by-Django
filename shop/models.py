from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    catagory = models.CharField(max_length=50, default="")
    subcatagory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    decs = models.CharField(max_length=350)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")


    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.IntegerField()
    message = models.CharField(max_length=3500)

    def __str__(self):
        return self.name