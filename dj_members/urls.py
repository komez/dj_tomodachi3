from django.urls import include,path
from django.contrib import admin
from django.conf import settings

#pathはURLと処理関数を対応させる関数（アプリケーション毎の'urls'を呼び出すことで整理できる）
#path の第二引数はview関数でもいい
urlpatterns = [
   path('accounts/', include('allauth.urls')), #追加
   path('games/', include('games.urls')),
   path('admin/', admin.site.urls),
]