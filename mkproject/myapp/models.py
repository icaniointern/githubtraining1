from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)  #short text
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    joined_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    username = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='')    # stores image
    resume = models.FileField(upload_to='')      # stores any file


class Student(models.Model):
    name  = models.CharField(max_length=100)
    age   = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name   
    


class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class new_profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        bio = models.TextField(blank=True)
        phone = models.CharField(max_length=13,blank=True)

        def __str__(self):
            return f"{self.user.username}'s newprofile"
    
    
