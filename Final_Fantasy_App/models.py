from django.db import models
from django import forms

# Create your models here.


class Character(models.Model):
    Name = models.CharField(max_length=255)
    Portrait = models.CharField(max_length=500)
    Avatar = models.CharField(max_length=500)
    characterId = models.CharField(max_length=500, default="3")

    def __str__(self):
        return self.Name


class GearPiece(models.Model):
    GEAR_TYPE_CHOICES = (
        ('Body', 'Body'),
        ('Bracelets', 'Bracelets'),
        ('Earrings', 'Earrings'),
        ('Head', 'Head'),
        ('Feet', 'Feet'),
        ('Hands', 'Hands'),
        ('Legs', 'Legs'),
        ('MainHand', 'Main Hand'),
        ('OffHand', 'Off Hand'),
        ('Necklace', 'Necklace'),
        ('Ring1', 'Ring 1'),
        ('Ring2', 'Ring 2'),
        ('SoulCrystal', 'Soul Crystal'),
        ('Waist', 'Waist')
    )
    Name = models.CharField(max_length=255, default='name')
    Creator = models.CharField(max_length=255, null=True)
    Icon = models.CharField(max_length=255, default='http://i.imgur.com/SwBRFdO.png')
    Dye = models.CharField(max_length=255, null=True)
    ID = models.AutoField(primary_key = True)
    Mirage = models.CharField(max_length=255, null=True)
    Character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='GearPieces')
    gearType = models.CharField(max_length=255, choices=GEAR_TYPE_CHOICES)

    def __str__(self):
        return self.Name

class WantedGear(models.Model):
    GEAR_TYPE_CHOICES = (
        ('Body', 'Body'),
        ('Bracelets', 'Bracelets'),
        ('Earrings', 'Earrings'),
        ('Head', 'Head'),
        ('Feet', 'Feet'),
        ('Hands', 'Hands'),
        ('Legs', 'Legs'),
        ('MainHand', 'Main Hand'),
        ('OffHand', 'Off Hand'),
        ('Necklace', 'Necklace'),
        ('Ring1', 'Ring 1'),
        ('Ring2', 'Ring 2'),
        ('SoulCrystal', 'Soul Crystal'),
        ('Waist', 'Waist')
    )
    Icon = models.CharField(max_length=255, default='http://i.imgur.com/SwBRFdO.png')
    Dye = models.CharField(max_length=255)
    ID = models.AutoField(primary_key = True)
    Mirage = models.CharField(max_length=255)
    Character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='wantedgear')
    gearType = models.CharField(max_length=255, choices=GEAR_TYPE_CHOICES)

    def __str__(self):
        return self.Icon

