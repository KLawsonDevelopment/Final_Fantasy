from rest_framework import serializers
from .models import Character, Gear_Details, GearPiece, WantedGear

class WantedSerializer(serializers.ModelSerializer):
    class Meta:
        model = WantedGear
        fields = ('id', 'Name', 'Body', 'Bracelet', 'Earrings', 'Feet', 'Hands', 'Head', 'Legs', 'MainHand', 'Necklace', 'Ring1', 'Ring2', 'Soul Crystal', 'Waist')
        

class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GearPiece
        fields = ('Creator', 'Dye', 'ID', 'Materia', 'Mirage', 'Icon')

class DetailSerializer(serializers.ModelSerializer):
    pieces = PieceSerializer(many=True, read_only=True)
    class Meta:
        model = Gear_Details
        fields = ('id', 'Name', 'Body', 'Bracelet', 'Earrings', 'Feet', 'Hands', 'Head', 'Legs', 'MainHand', 'Necklace', 'Ring1', 'Ring2', 'Soul Crystal', 'Waist')

class CharacterSerializer(serializers.ModelSerializer):
    gear = DetailSerializer(many=True, read_only=True)
    wanted = WantedSerializer(many=True, read_only=True)
    class Meta:
        model = Character
        fields = ('id', 'Name', 'Portrait', 'Avatar', 'gear', 'wanted')
