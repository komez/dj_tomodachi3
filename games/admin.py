from django.contrib import admin
from .models import Team, Profile
from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)

admin.site.register(Profile)
admin.site.register(Team)