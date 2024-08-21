from django.shortcuts import render,redirect
from .forms import RegisterForm, CustomerDatabase, EarnCustomerData, profiles, social_group
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomerList,EarnCustomer, profiledetails, social_media_data
from django.db.models import Sum
from categories.forms import category_items
from categories.models import category, product
from django.http.response import JsonResponse, HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm


# Create your views here.

@login_required
def home(request):
      form = User.objects.all()
      data = form.count()

      form1 = CustomerList.objects.all()
      data1 = form1.count()

      data2 = EarnCustomer.objects.all()
      total = data2.aggregate(total_price=Sum('price'))['total_price']
      
      data3 = social_media_data.objects.all().count()
      
      context = {'data': data, 'data1': data1, 'total': total, 'data3':data3}
      return render(request, 'index.html', context)

@login_required
def home_base(request):
      # data = registerCustomer.objects.all()
      # form = User.objects.all()
      # context = {'data': data}
      return render(request, 'base.html')


# def signup_view(request):
#       form = RegisterForm()
#       if request.method == 'POST':
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                   form.save()
#                   messages.success(request, 'Your registration was successfully saved.')
#                   return redirect('signup_view')
#             else:
#                   form = RegisterForm()
#                   messages.error(request, 'Invaild Your registration was failed. Please try again.')
#       else:
#             form = RegisterForm()
#       context = {'form': form}
#       return render(request, 'signup.html', context)

# def signup_view(request):
#       form = RegisterForm()
#       if request.method == 'POST':
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                   if User.objects.filter(username=form.cleaned_data.get('username')).exists():
#                         messages.error(request, 'Username is already taken.')
#                         return redirect('signup_view')
#                   form.save()
#                   messages.success(request, 'Registration successful! Please log in.')    
#                   return redirect('login_view')  # Replace with your login view name
#             else:
#                   messages.error(request, form.errors)  # Display form errors
#       context = {'form': form}
#       return render(request, 'signup.html', context)

class RegisterForm(UserCreationForm):
      class Meta(UserCreationForm.Meta):
            error_messages = {
                  'username' : {
                        'unique' : 'Username is already taken. Please choose another username.'
                  },
                  
                  'password2' : {
                        'Password_mismatch' : 'This two password do not match.'
                  },
            }
            
def signup_view(request):
      if request.method == 'POST':
            form = RegisterForm(request.POST)
            try:
                  if form.is_valid():
                        user = form.save()
                        login(request, user)
                        messages.success(request, 'Signup success. Welcome!')
                        return redirect('signin_view')
                  else:
                        for field, errors in form.errors.items():
                              for error in errors:
                                    messages.error(request, f'{field.capitalize()}: {error}')
            except Exception as e:
                  messages.error(request, f'Signup faild. An error occured. : {str(e)}')
      else:
            form = RegisterForm()
      context = {'form': form}
      return render(request, 'signup.html', context)



# def signin_view(request):
#       if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password1')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                   login(request, user)
#                   return redirect('home')
#             else:
#                   return redirect('signin_view')
#       return render(request, 'signin.html')

def signin_view(request):
      if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                  username = form.cleaned_data.get('username')
                  password = form.cleaned_data.get('password')
                  user = authenticate(username=username, password=password)
                  if user is not None:
                        login(request, user)
                        messages.success(request, 'Login successfully. Welcome Back!')
                        return redirect('home')  # Replace 'home' with the name of your home page URL pattern
                  else:
                        messages.error(request, 'Invalid Username or Password.')
            else:
                  messages.error(request, 'Invalid Username or Password.')
      else:
            form = AuthenticationForm()
      context = {'form': form}
      return render(request, 'signin.html', context)

@login_required
def logout_view(request):
      logout(request)
      return redirect('signin_view')

# @login_required
# def data_profile(request):
#       data = User.objects.all()
#       context = {'data': data}
#       return render(request, 'data_profile.html', context)

@login_required
def customerform(request):
      data = CustomerDatabase()
      if request.method == 'POST':
            data = CustomerDatabase(request.POST)
            if data.is_valid():
                  data.save()
                  return redirect('customer_table')
      return render(request, 'customerform.html', {'data': data})

@login_required
def customer_table(request):
      form = CustomerList.objects.all()
      context = {'form': form}
      return render(request, 'customer_table.html', context)

# JSON DATA
@login_required
def customer_table_data(_request):
      programdata = list(CustomerList.objects.values())
      data  = {'programdata': programdata}
      return JsonResponse(data)

def customer_table_data_json(request):
      return render(request, 'customer_table2.html')


@login_required
def editCustomer(request, pk):
      
      form = CustomerList.objects.get(id=pk)
      data = CustomerDatabase(request.POST or None, instance=form)
      if data.is_valid():
            data.save()
            return redirect('customer_table')
      return render(request, 'edit_customer.html', {'data': data})


@login_required
def deleteCustomer(request, pk):
      form = CustomerList.objects.get(id=pk)
      form.delete()
      return redirect('customer_table')

@login_required
def user_data(request):
      form = RegisterForm()
      data = User.objects.all()
      if request.method == 'POST':
            form = RegisterForm(request.POST)
            
            if form.is_valid():
                  username = form.cleaned_data['username']
            
                  if User.objects.filter(username=username).exists():
                        messages.error(request, 'Username already taken. Please choose a different username.')
                  else:
                        user = User.objects.create_user(
                              username=username,
                              password=form.cleaned_data.get['password1'],
                              email=form.cleaned_data.get['email'],
                              first_name=form.cleaned_data.get['first_name'],
                              last_name=form.cleaned_data.get['last_name'],
                        )
                        user.is_staff = form.cleaned_data.get('is_staff', False)
                        user.is_active = form.cleaned_data.get('is_active', True)
                        user.is_superuser = form.cleaned_data.get('is_superuser', False)
                        user.save()
                        messages.success(request, 'Your registration was successfully saved.')
                        return redirect('userdata')
            else:
                  print(form.errors)

      context = {'form': form, 'data': data}
      return render(request, 'user_data.html', context)

@login_required
def earningCustomer(request):
      data = EarnCustomer.objects.all()
      total = data.aggregate(Sum('price'))
      # total_payments = data.aggregate(total_price=Sum('price'))['total_price']
      context = {'data': data , 'total': total}
      return render(request, 'earning.html', context)

@login_required
def registerearning(request):
      data = EarnCustomerData()
      if request.method == 'POST':
            data = EarnCustomerData(request.POST)
            if data.is_valid():
                  data.save()
            return redirect('earningCustomer')
      context = {'data': data}
      return render(request, 'register_earning.html', context)

@login_required
def profile_filter(request):
      user = request.user
      try:
            profile = profiledetails.objects.get(user=user)
      except profiledetails.DoesNotExist:
            profile = None
      context = {'user': user, 'profile': profile}
      return render(request, 'profile_filter.html', context)

@login_required
def category_register(request):
      # data = category_items()
      if request.method == 'POST':
            data = category_items(request.POST, request.FILES)
            if data.is_valid():
                  data.save()
                  return redirect('category_show')
      else:
            data = category_items()
      context = {'data': data}
      return render(request, 'category_register.html', context)

@login_required
def sub_category_register(request):
      return render(request, 'sub_cateRegister.html')

@login_required
def category_show(request):
      data = category.objects.filter(status=True)
      context = {'data': data}
      return render(request, 'category.html', context)

@login_required
def sub_category(request, id):
      data = product.objects.filter(subcategory=id)
      return render(request, 'sub_category.html', {'data': data})


def socical_media(request):
      data1 = social_media_data.objects.all()
      
      if request.method == 'POST':
            data = social_group(request.POST , request.FILES)
            if data.is_valid():
                  data.save()
                  messages.success(request, 'Successfully Added.')
                  return redirect('socical_media')
      else:
            data = social_group()  
      context = {'data': data , 'data1' : data1}
      return render(request, 'social_add.html', context)