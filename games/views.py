from django.shortcuts import render, redirect
from . forms import ProfileForm, TeamCreateForm
from .models import Profile, Team
# Create your views here.

def index(request):
    #(public_user, public_group) = get_public() 
    params={}
    return render(request, 'games/index.html')

#@login_required(login_url='/admin/login/')
def create(request):
    params={
        'name':'name',
        'msg':'プロフィールを入力してください',
        'form':ProfileForm(),
    }
    if (request.method == 'POST'):
        obj=Profile()
        obj.person=request.user
        obj.name=request.POST['name']
        obj.birthday=request.POST['birthday']
        if request.POST['choices']=='male':
            obj.gender='True'
        else:
            obj.gender='False'
        obj.hometown=request.POST['hometown']
        obj.school=request.POST['school']
        obj.hobby=request.POST['hobby']
        obj.food=request.POST['food']
        obj.thing=request.POST['thing']
        obj.hope=request.POST['hope']
        obj.text=request.POST['text']

        obj.save()
        return redirect(to='/games/')
       
    return render(request, 'games/create.html', params)

def edit(request):
    obj=Profile.objects.get(id=num)
    if (request.method=='POST'):
        Profile=ProfileForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/games')
    params={
        'title':'Hello',
        'form':ProfileForm(instance=obj)
    }
    return render(request, 'games/create.html', params)

def group_create(request):
    params={
        'form':TeamCreateForm(),
    }
    if (request.method == 'POST'):
        team=Team()
        team.owner=request.user
        team.team_name=request.POST['team_name']
        team.team_password=request.POST['team_password']
        team.save()
        
        return redirect(to='group_confirm')
    return render(request, 'games/group_create.html', params)

def group_confirm(request):
    return render(request, 'games/group_confirm.html')

def form(request):
    msg=request.POST['msg']#msgはhtml内でname='msg'で指定されたもの
    params = {
        'title':'games/Form',
        'msg':'こんにちは、'+ msg +'さん。',#msg はhtml内でid='msg'で指定されたもの

    }
    return render(request, 'games/profile.html', params)