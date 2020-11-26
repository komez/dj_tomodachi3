from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.login = login_required(admin.site.login)
admin.site.register(User)
