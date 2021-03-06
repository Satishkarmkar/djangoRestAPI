# Generated by Django 3.0.2 on 2020-07-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_studentregistrationmodel_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentEnrolledCourseModel',
            fields=[
                ('cno', models.IntegerField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('cdate', models.DateField()),
                ('ctime', models.TimeField()),
                ('fee', models.FloatField()),
                ('dur', models.IntegerField()),
            ],
        ),
    ]
