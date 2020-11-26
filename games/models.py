from django.db import models
from django import forms
from users.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class Team(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    team_password=models.CharField(max_length=225)
    team_name=models.CharField(max_length=225)
    #,validators=[MinLengthValidator(6)]
    def __str__(self):
        return self.team_name

class Profile(models.Model):
    #teamにつき一つのプロフィール
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    name =models.CharField(max_length=225)
    image=models.FileField(blank=True,upload_to='img/upload/{}'.format(User.id))
    birthday=models.DateField()
    gender=models.BooleanField()
    hometown=models.CharField(max_length=225)
    school=models.CharField(max_length=225)
    hobby=models.CharField(max_length=225)
    food=models.CharField(max_length=225)
    thing=models.CharField(max_length=225)
    hope=models.CharField(max_length=225)
    text=models.TextField(max_length=450)
    playcount=models.IntegerField(default=0)
    percentage=models.IntegerField(default=0)


class Choice(models.Model):
    description = models.CharField(max_length=225)

class Member(models.Model):
    #ownerいらない説
    owner = models.ForeignKey(User,on_delete=models.CASCADE,#オーナーがいなくなったら消す？→オーナーがアカウント消すとき忠告する仕組みを作る
        related_name='member_owner')#allauthの方でオーナーは設定できないかな
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Team, on_delete=models.CASCADE)
    affiliation=models.OneToOneField(Choice, on_delete=models.SET_NULL, null=True)#リストにしたい新卒、営業、など
    def __str__(self):
        return str(self.user) + '(group:"'+str(self.group) + '"'