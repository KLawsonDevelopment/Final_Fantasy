# Generated by Django 2.2 on 2019-04-16 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Portrait', models.CharField(max_length=500)),
                ('Avatar', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Gear_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='name', max_length=255)),
                ('Body', models.CharField(max_length=255)),
                ('Bracelets', models.CharField(max_length=255)),
                ('Earrings', models.CharField(max_length=255)),
                ('Feet', models.CharField(max_length=255)),
                ('Hands', models.CharField(max_length=255)),
                ('Head', models.CharField(max_length=255)),
                ('Legs', models.CharField(max_length=255)),
                ('MainHand', models.CharField(max_length=255)),
                ('Necklace', models.CharField(max_length=255)),
                ('Ring1', models.CharField(max_length=255)),
                ('Ring2', models.CharField(max_length=255)),
                ('SoulCrystal', models.CharField(max_length=255)),
                ('Waist', models.CharField(max_length=255)),
                ('Character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gear_details', to='Final_Fantasy_App.Character')),
            ],
        ),
        migrations.CreateModel(
            name='WantedGear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Body', models.CharField(max_length=255)),
                ('Bracelets', models.CharField(max_length=255)),
                ('Earrings', models.CharField(max_length=255)),
                ('Feet', models.CharField(max_length=255)),
                ('Hands', models.CharField(max_length=255)),
                ('Head', models.CharField(max_length=255)),
                ('Legs', models.CharField(max_length=255)),
                ('MainHand', models.CharField(max_length=255)),
                ('Necklace', models.CharField(max_length=255)),
                ('Ring1', models.CharField(max_length=255)),
                ('Ring2', models.CharField(max_length=255)),
                ('SoulCrystal', models.CharField(max_length=255)),
                ('Waist', models.CharField(max_length=255)),
                ('Character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wanted_gear', to='Final_Fantasy_App.Character')),
            ],
        ),
        migrations.CreateModel(
            name='GearPiece',
            fields=[
                ('Creator', models.CharField(max_length=255)),
                ('Dye', models.CharField(max_length=255)),
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Materia', models.CharField(max_length=255)),
                ('Mirage', models.CharField(max_length=255)),
                ('gearType', models.CharField(choices=[('Body', 'Body'), ('Bracelets', 'Bracelets'), ('Earrings', 'Earrings'), ('Feet', 'Feet'), ('Hands', 'Hands'), ('Head', 'Head'), ('Legs', 'Legs'), ('MainHand', 'Main Hand'), ('Necklace', 'Necklace'), ('Ring1', 'Ring 1'), ('Ring2', 'Ring2'), ('SoulCrystal', 'Soul Crystal'), ('Waist', 'Waist')], default='Body', max_length=255)),
                ('Gear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GearPieces', to='Final_Fantasy_App.Gear_Details')),
            ],
        ),
    ]
