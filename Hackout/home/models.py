from django.db import models

# Create your models here.

class data_set(models.Model):
    full_name = models.CharField(max_length=150)
    ph_no = models.CharField(max_length=10,unique=True,primary_key=True)
    profession = models.CharField(max_length=50)
    email  = models.EmailField(unique=True)



    def __str__(self):
        return self.full_name



class CropDetails(models.Model):
    crop_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    due_date = models.DateField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.crop_name