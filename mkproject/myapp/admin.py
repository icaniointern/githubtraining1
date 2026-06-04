from django.contrib import admin

# Regisfrom django.contrib import admin
from .models import Product,customer,Profile,Student,new_profile,user

admin.site.register(Product)   # ← to manage posts in admin panelter your models here.
admin.site.register(customer)
admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(new_profile)
admin.site.register(user)