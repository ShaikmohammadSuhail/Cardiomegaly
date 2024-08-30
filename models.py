from django.db import models
import os
# Create your models here.




class Register(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
    age=models.CharField(max_length=50,null=True)
    contact=models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=30,null=True)
    class Meta:
        db_table = "UserRegistration"

class Cardio(models.Model):
    image=models.ImageField(upload_to="app/static/saved")

    def filename(self):
        return os.path.basename(self.image.name) 