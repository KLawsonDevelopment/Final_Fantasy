from django.contrib import admin
from .models import Character, WantedGear, GearPiece

# Register your models here.

admin.site.register([Character, GearPiece, WantedGear])