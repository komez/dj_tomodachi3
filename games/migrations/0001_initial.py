# Generated by Django 2.2.5 on 2020-11-26 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_password', models.CharField(max_length=225)),
                ('team_name', models.CharField(max_length=225)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('image', models.FileField(blank=True, upload_to='img/upload/<django.db.models.query_utils.DeferredAttribute object at 0x000002CE6730E5F8>')),
                ('birthday', models.DateField()),
                ('gender', models.BooleanField()),
                ('hometown', models.CharField(max_length=225)),
                ('school', models.CharField(max_length=225)),
                ('hobby', models.CharField(max_length=225)),
                ('food', models.CharField(max_length=225)),
                ('thing', models.CharField(max_length=225)),
                ('hope', models.CharField(max_length=225)),
                ('text', models.TextField(max_length=450)),
                ('playcount', models.IntegerField(default=0)),
                ('percentage', models.IntegerField(default=0)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affiliation', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='games.Choice')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Team')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_owner', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
