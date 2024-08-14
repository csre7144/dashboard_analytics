from django.contrib import admin
from .models import CustomerList, EarnCustomer,profiledetails, social_media_data

# Register your models here.
admin.site.register(CustomerList)
admin.site.register(EarnCustomer)
admin.site.register(profiledetails)
admin.site.register(social_media_data)