# Generated by Django 2.2 on 2019-04-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Final_Fantasy_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wantedgear',
            name='Name',
            field=models.CharField(default='name', max_length=255),
        ),
    ]
