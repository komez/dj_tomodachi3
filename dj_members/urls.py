from django.urls import include,path
from django.contrib import admin
from django.conf import settings
urlpatterns = [
   path('accounts/', include('allauth.urls')), #追加
   path('games/', include('games.urls')),
   path('admin/', admin.site.urls),
]