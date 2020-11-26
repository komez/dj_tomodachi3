from django import forms
from django.db import models
from users.models import User
#from .models import Profile, Group

class ProfileForm(forms.Form):
    data=[
        ('one','male'),
        ('two','female')
    ]
    #person= models.ForeignKey(User, on_delete=models.CASCADE)
    name =forms.CharField(max_length=225)
    birthday=forms.DateField()
    choices=forms.ChoiceField(choices=data)
    hometown=forms.CharField(max_length=225)
    school=forms.CharField(max_length=225)
    hobby=forms.CharField(max_length=225)
    food=forms.CharField(max_length=225)
    thing=forms.CharField(max_length=225)
    hope=forms.CharField(max_length=225)
    text=forms.CharField(widget=forms.Textarea,max_length=225)

    def clean(self):
        cleaned_data=super().clean()
        str = cleaned_data['name']
        if 'name'=='komezakiryouta':
            raise forms.ValidationError
            
class TeamCreateForm(forms.Form):
    team_name=forms.CharField(max_length=50)
    team_password=forms.CharField(max_length=20, min_length=6)

class TeamCustomForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(TeamCustomForm, self).__init__(*args, **kwargs)
        self.fields['team_custom']=forms.ChoiceField()


    