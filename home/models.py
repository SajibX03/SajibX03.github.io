from django.db import models

# Create your models here.
class contact (models.Model):
    firstName = models.CharField(max_length=100)
    lastName =  models.CharField(max_length=100)
    email =  models.EmailField()
    Text = models.CharField(max_length=500)
    date= models.DateField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"