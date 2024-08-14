from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup_view/', views.signup_view, name='signup_view'),
    # path("check_user/",views.check_user,name="check_user"),
    path('', views.signin_view, name='signin_view'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), 
    path('customerform/', views.customerform, name='customerform'),
    path('customer_table/', views.customer_table, name='customer_table'),
    path('editCustomer/<int:pk>', views.editCustomer, name='editCustomer'),
    path('deleteCustomer/<int:pk>', views.deleteCustomer, name='deleteCustomer'),
    path('user_data/', views.user_data, name='user_data'),
    path('earningCustomer/', views.earningCustomer, name='earningCustomer'),
    path('registerearning/', views.registerearning, name='registerearning'),
    path('profile_filter/', views.profile_filter, name='profile_filter'),
    path('category_show/', views.category_show, name='category_show'),
    path('sub_category/<int:id>', views.sub_category, name='sub_category'),
    path('category_register/', views.category_register, name='category_register'),
    path('sub_category_register/', views.sub_category_register, name='sub_category_register'),
    path('customer_table_data_json/', views.customer_table_data_json, name='customer_table_data_json'),
    path('app/customer_table_data/', views.customer_table_data, name='customer_table_data'),
    path('socical_media/', views.socical_media, name='socical_media'),
    # path('socical_media/<int:pk>', views.socical_media, name='socical_media'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
