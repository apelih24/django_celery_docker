# Generated by Django 2.0.7 on 2018-07-25 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IcoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ico_scale', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
    ]