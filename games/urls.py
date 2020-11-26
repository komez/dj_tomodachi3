from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('form',views.form, name='form'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('group_create', views.group_create, name='group_create'),
    path('group_confirm', views.group_confirm, name='group_confirm'),
    #path('member_')
]