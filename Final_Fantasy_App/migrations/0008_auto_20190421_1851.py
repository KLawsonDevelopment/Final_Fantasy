# Generated by Django 2.2 on 2019-04-21 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Final_Fantasy_App', '0007_auto_20190421_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gearpiece',
            name='Creator',
            field=models.CharField(default='creator', max_length=255),
        ),
        migrations.AlterField(
            model_name='gearpiece',
            name='Dye',
            field=models.CharField(default='dye', max_length=255),
        ),
        migrations.AlterField(
            model_name='gearpiece',
            name='Mirage',
            field=models.CharField(default='dye', max_length=255),
        ),
    ]