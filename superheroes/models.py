from django.db import models

# Create your models here.
class Publisher(models.Model):
    name=models.CharField(max_length=100,blank=True,default='')
    founder=models.CharField(max_length=100,blank=True,default='')

    def __str__(self):
        return self.name

class SuperHeroe(models.Model):
    name=models.CharField(max_length=100,blank=True,default='')
    gender=models.CharField(max_length=100,blank=True,default='')
    real_name=models.CharField(max_length=100,blank=True,default='')
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)

    def __str__(self):
        return self.name