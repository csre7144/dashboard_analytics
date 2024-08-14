from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CustomerList(models.Model):
      first_name = models.CharField(max_length=50)
      last_name = models.CharField(max_length=50)
      email = models.EmailField(max_length=50)
      phone = models.CharField(max_length=10)
      city = models.CharField(max_length=20)

      def __str__(self):
            return self.first_name + ' ' + self.last_name
      

class EarnCustomer(models.Model):
      fname = models.CharField(max_length=50)
      lname = models.CharField(max_length=50)
      date = models.DateField(blank=True, null=True)
      price = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
      create_time = models.DateTimeField(auto_now_add=True)

      def __str__(self) -> str:
            return self.fname + ' ' + self.lname
      
class profiledetails(models.Model):
      Male = "Male"
      Female = "Female"
      gender_choices = (
            (Male, "Male"),
            (Female, "Female")
      )
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      gender = models.CharField(max_length=7, choices=gender_choices, default=Male)
      address = models.CharField(max_length=255)
      pincode = models.CharField(max_length=6)

      def __str__(self):
            return f"{self.user.username}'s Profile"
      

class social_media_data(models.Model):
      subject_name = models.CharField(max_length=30)
      description = models.TextField(max_length=100000)
      img = models.ImageField(upload_to='img/social_media/')

      def __str__(self):
          return self.subject_name
      