# Generated by Django 3.0.2 on 2020-07-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200718_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentregistrationmodel',
            name='spasswd',
        ),
        migrations.RemoveField(
            model_name='studentregistrationmodel',
            name='suname',
        ),
        migrations.AddField(
            model_name='studentregistrationmodel',
            name='uname',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='studentregistrationmodel',
            name='upass',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
