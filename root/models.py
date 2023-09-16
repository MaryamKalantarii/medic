from django.db import models
import datetime
from accounts.models import CustomeUser



class Building(models.Model):
     title = models.CharField(max_length=100)
     content=models.TextField()
     status = models.BooleanField(default=False)
     image = models.ImageField(upload_to='building', default='building.jpg')


class NewsLetter (models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email



class Services (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_data']

class HealthService(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.title



class Skills(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class Doctor(models.Model):
    info = models.ForeignKey(CustomeUser , on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    image = models.ImageField(upload_to='doctor', default='doctor.jpg')
    twitter = models.CharField(max_length=255, default='#')
    facebook = models.CharField(max_length=255, default='#')
    instagram = models.CharField(max_length=255, default='#')
    linkdin = models.CharField(max_length=255, default='#')
    status = models.BooleanField(default=False)
    

    def __str__(self):
        return self.info.username




class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.name
