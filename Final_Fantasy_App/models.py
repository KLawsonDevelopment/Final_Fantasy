from django.db import models

# Create your models here.


class Character(models.model):
    Name = models.CharField(max_length=255)
    Portrait = models.CharField(max_length=500)
    Avatar = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Gear_Details(models.model):
    Body = models.CharField(max_length=255)
    Bracelets = models.CharField(max_length=255)
    Earrings = models.CharField(max_length=255)
    Feet = models.CharField(max_length=255)
    Hands = models.CharField(max_length=255)
    Head = models.CharField(max_length=255)
    Legs = models.CharField(max_length=255)
    MainHand = models.CharField(max_length=255)
    Necklace = models.CharField(max_length=255)
    Ring1 = models.CharField(max_length=255)
    Ring2 = models.CharField(max_length=255)
    SoulCrystal = models.CharField(max_length=255)
    Waist = models.CharField(max_length=255)
    Character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='gear_details')

    def __str__(self):
        return self.Character

class GearPiece(models.model):
    Creator = models.CharField(max_length=255)
    Dye = models.CharField(max_length=255)
    ID = models.IntegerField(max_length=255)
    Materia = models.CharField(max_length=255)
    Mirage = models.CharField(max_length=255)
    Gear = models.ManyToManyField(Gear_Details)

    def __str__(self):
        return self.Gear

class WantedGear(models.model):
    Body = models.CharField(max_length=255)
    Bracelets = models.CharField(max_length=255)
    Earrings = models.CharField(max_length=255)
    Feet = models.CharField(max_length=255)
    Hands = models.CharField(max_length=255)
    Head = models.CharField(max_length=255)
    Legs = models.CharField(max_length=255)
    MainHand = models.CharField(max_length=255)
    Necklace = models.CharField(max_length=255)
    Ring1 = models.CharField(max_length=255)
    Ring2 = models.CharField(max_length=255)
    SoulCrystal = models.CharField(max_length=255)
    Waist = models.CharField(max_length=255)
    Character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='gear_details')

    def __str__(self):
        return self.Character

