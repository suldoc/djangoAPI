from rest_framework import serializers
from .models import Taste_note

class SuldocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taste_note
        fields = ('id', 'user_id', 'name', 'comment', 'stars_taste', 'stars_costvalue', 'img_path')