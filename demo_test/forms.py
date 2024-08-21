from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomerList, EarnCustomer,profiledetails,social_media_data
from django import forms

class RegisterForm(UserCreationForm):
      first_name = forms.CharField(max_length=30, required=True)
      last_name = forms.CharField(max_length=30, required=True)
      email = forms.EmailField(max_length=254, required=True, help_text='Required')
      is_active = forms.BooleanField(label='Active', required=False)
      is_staff = forms.BooleanField(label='Staff', required=False)
      is_superuser = forms.BooleanField(label='Superuser', required=False)
      
      class Meta:
            model = User
            fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser']

      
      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["first_name"].widget.attrs.update({"class": "form-control", "placeholder":"First Name"})
            self.fields["last_name"].widget.attrs.update({"class": "form-control", "placeholder":"Last Name"})
            self.fields["username"].widget.attrs.update({"class": "form-control", "placeholder":"Username"})
            self.fields["email"].widget.attrs.update({"class": "form-control", "placeholder":"Email"})
            self.fields["password1"].widget.attrs.update({"class": "form-control", "placeholder":"Password"})
            self.fields["password2"].widget.attrs.update({"class": "form-control", "placeholder":"Re-Type Password"})
            # self.fields["Photo"].widget.attrs.update({"class": "form-control"})

class CustomerDatabase(forms.ModelForm):
      first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
      last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
      email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
      phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
      city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
      
      class Meta:
            model = CustomerList
            exclude = ("user",)
            # fields = '__all__'

class EarnCustomerData(forms.ModelForm):
      fname = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
      lname = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
      date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"placeholder":"Date Pay", "class":"form-control", "type":"Date"}), initial="26-07-2024")
      price = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Pay", "class":"form-control"}), label="")


      class Meta:
            model = EarnCustomer
            fields = '__all__'


class profiles(forms.ModelForm):
      class Meta:
            model = profiledetails
            fields = '__all__'

      # def __init__(self, *args, **kwargs):
      #       super().__init__(*args, **kwargs)
      #       self.fields["question"].widget.attrs.update({"class": "form-control", "placeholder":"First Name"})
      #       self.fields["gender"].widget.attrs.update({"class": "form-control", "placeholder":"First Name"})
      #       self.fields["address"].widget.attrs.update({"class": "form-control", "placeholder":"First Name"})
      #       self.fields["pincode"].widget.attrs.update({"class": "form-control", "placeholder":"First Name"})



class social_group(forms.ModelForm):
      class Meta:
            model = social_media_data
            fields = '__all__'