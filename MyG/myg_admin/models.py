from django.db import models

# Create your models here.
class Appliences(models.Model):
    applience_name=models.CharField(unique=True,max_length=100)
    copies=models.PositiveIntegerField(null=True,default=1000)
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.Applience_name