from django.db import models
from embed_video.fields import EmbedVideoField

class Placements(models.Model):
    video = EmbedVideoField()  # same like models.URLField()


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phoneNumber=models.BigIntegerField()
    subject=models.CharField(max_length=100)
    message=models.TextField(default='',blank=True, null=True)

    def __str__(self):
        return f'Message from {self.name}'
    
class Blogs(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    authname=models.CharField(max_length=50)
    img=models.ImageField(upload_to='images',blank='True',null='True')
    timeStamp=models.DateTimeField(auto_now_add='True')

    def __str__(self):
        return f'Uploaded by {self.authname}'

class Courses(models.Model):
    title=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics',blank='True',null='True')

    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    img=models.ImageField(upload_to='Gallery',blank='True',null='True')
    timeStamp=models.DateTimeField(auto_now_add='True')

  
    def __int__(self):
        return self.img

   
   
class Registration(models.Model):
    reservation_name=models.CharField(max_length=55)
    reservation_email=models.EmailField()
    reservation_phone=models.BigIntegerField()
    select_course=models.CharField(max_length=55)
    Date=models.DateField()
    form_message=models.TextField(default='',blank=True, null=True)

    def __str__(self):
        return self.reservation_name

   



     