from rest_framework import serializers
from .models import Character, GearPiece, WantedGear

class WantedSerializer(serializers.ModelSerializer):
    class Meta:
        model = WantedGear
        fields = '__all__'
        

class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GearPiece
        fields = '__all__'

# class DetailSerializer(serializers.ModelSerializer):
#     GearPieces = PieceSerializer(many=True, read_only=True)
#     class Meta:
#         model = Gear_Details
#         fields = '__all__'

class CharacterSerializer(serializers.ModelSerializer):
    # gear_details = DetailSerializer(many=True, read_only=True)
    GearPieces = PieceSerializer(many=True, read_only=True)
    wantedgear = WantedSerializer(many=True, read_only=True)
    class Meta:
        model = Character
        fields = '__all__'
