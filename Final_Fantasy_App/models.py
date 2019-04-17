from django.db import models
from django import forms

# Create your models here.


class Character(models.Model):
    Name = models.CharField(max_length=255)
    Portrait = models.CharField(max_length=500)
    Avatar = models.CharField(max_length=500)

    def __str__(self):
        return self.Name


# class Gear_Details(models.Model):
#     Name = models.CharField(max_length=255, default="name")
#     Body = models.CharField(max_length=255, default="body")
#     Bracelets = models.CharField(max_length=255, default="Bracelets")
#     Earrings = models.CharField(max_length=255, default="Earrings")
#     Feet = models.CharField(max_length=255, default="Feet")
#     Hands = models.CharField(max_length=255, default="Hands")
#     Head = models.CharField(max_length=255, default="Head")
#     Legs = models.CharField(max_length=255, default="Legs")
#     MainHand = models.CharField(max_length=255, default="MainHand")
#     Necklace = models.CharField(max_length=255, default="Necklace")
#     Ring1 = models.CharField(max_length=255, default="Ring1")
#     Ring2 = models.CharField(max_length=255, default="Ring2")
#     SoulCrystal = models.CharField(max_length=255, default="SoulCrystal")
#     Waist = models.CharField(max_length=255, default="Waist")
#     Character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='gear_details')

#     def __get_tuple(self):
#         return (
#             (self.Body,
#             self.Bracelets,
#             self.Earrings,
#             self.Feet,
#             self.Hands,
#             self.Legs,
#             self.MainHand,
#             self.Necklace,
#             self.Ring1,
#             self.Ring2,
#             self.SoulCrystal,
#             self.Waist),
#         )
    
#     def __getitem__(self):
#         return self.__get_tuple()[key]

#     def __iter__(self):
#         return iter(self.__get_tuple())

#     def __str__(self):
#         return self.Name

class GearPiece(models.Model):
    GEAR_TYPE_CHOICES = (
        ('body', 'Body'),
        ('bracelets', 'Bracelets')
    )
    Creator = models.CharField(max_length=255)
    Icon = models.CharField(max_length=255, default='http://i.imgur.com/SwBRFdO.png')
    Dye = models.CharField(max_length=255)
    ID = models.AutoField(primary_key = True)
    Materia = models.CharField(max_length=255)
    Mirage = models.CharField(max_length=255)
    # Gear = models.ForeignKey(Gear_Details, on_delete=models.CASCADE, related_name='GearPieces')
    Character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='GearPieces')
    gearType = models.CharField(max_length=255, choices=GEAR_TYPE_CHOICES)

    def __str__(self):
        return self.Creator

class WantedGear(models.Model):
    GEAR_TYPE_CHOICES = (
        ('body', 'Body'),
        ('bracelets', 'Bracelets')
    )
    Icon = models.CharField(max_length=255, default='http://i.imgur.com/SwBRFdO.png')
    Dye = models.CharField(max_length=255)
    ID = models.AutoField(primary_key = True)
    Materia = models.CharField(max_length=255)
    Mirage = models.CharField(max_length=255)
    Character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='wantedgear')
    gearType = models.CharField(max_length=255, choices=GEAR_TYPE_CHOICES)

    def __str__(self):
        return self.Icon

