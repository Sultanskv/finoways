from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
import uuid


# class MyAccountManager(BaseUserManager):
#     def create_user(self, user_id,is_employee=True,is_employer=False, password=None):
#         if not user_id:
#             raise ValueError('Users must have a userID')

#         user = self.model(
#             user_id=user_id,
#             is_client = is_client,
#             is_client = is_client,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
    # def create_superuser(self, user_id, is_client=False, is_client=False,email="xyz@gmail.com", password=None):
    #     user = self.create_user(
    #         user_id=user_id,
    #         is_employee = False,
    #         is_employer = False,
    #         password=password,
    #     )
    #     user.email=email
    #     user.is_admin = True
    #     user.is_staff = True
    #     user.is_superuser = True
    #     user.save(using=self._db)
    #     return user


class Account(AbstractBaseUser):
    user_id = models.IntegerField(verbose_name="user_id",  unique=True, primary_key=True)
    is_client = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    email = models.EmailField(blank=True,null=True,verbose_name='email')
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)


    # USERNAME_FIELD = 'user_id'
    # REQUIRED_FIELDS = ['is_client','is_client']

    # objects = MyAccountManager()

    # def __str__(self):
    #     return str(self.user_id)

	# # For checking permissions. to keep it simple all admin have ALL permissons
    # def has_perm(self, perm, obj=None):
    #     return self.is_admin

	# # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    # def has_module_perms(self, app_label):
    #     return True

# class ClientDetail(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     clientcode = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.user.username   


class ClientDetail(models.Model):
    user_id = models.CharField(max_length=8, unique=True, default=uuid.uuid4().hex[:8])
 #   user_id = models.IntegerField(verbose_name="user_id",  unique=True, primary_key=True)
    name_first = models.CharField(max_length=50, blank=True, null=True)
    name_last = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=50,blank=True, null=True)
    phone_number = models.CharField(max_length=15,blank=True, null=True)
    verify_code = models.CharField(max_length=15,blank=True, null=True)

    date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login= models.DateTimeField(verbose_name='last login', auto_now=True)
 
    is_staff= models.BooleanField(default=False)
    


from django.contrib.auth.models import User
from django.db import models

class ClientSignal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , blank=True, null=True)
  
    client_id = models.CharField(max_length=50, blank=True, null=True)
    message_id = models.CharField(max_length=50, blank=True, null=True)
    ids = models.CharField(max_length=50, blank=True, null=True)
    SYMBOL_CHOICES = (
        ('EUR/USD', 'EUR/USD'),
        ('USD/JPY', 'USD/JPY'),
        ('XAU/USD', 'XAU/USD'),
        ('GBP/USD', 'GBP/USD'),
    )
    SYMBOL = models.CharField(max_length=10, choices=SYMBOL_CHOICES)
    TYPE_CHOICES = (
        ('BUY_ENTRY', 'BUY_ENTRY'),
        ('BUY_EXIT', 'BUY_EXIT'),
        ('SELL_ENTRY', 'SELL_ENTRY'),
        ('SELL_EXIT', 'SELL_EXIT'),
    )
    TYPE = models.CharField(max_length=10, choices=TYPE_CHOICES)
    QUANTITY = models.PositiveIntegerField(null=True, blank=True)
    ENTRY_PRICE = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    EXIT_PRICE = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    profit_loss =  models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    cumulative_pl =  models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
  
