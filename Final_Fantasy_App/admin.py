from django.contrib import admin
from .models import Character, WantedGear, Gear_Details, GearPiece

# Register your models here.

admin.site.register([Character, Gear_Details, GearPiece, WantedGear])