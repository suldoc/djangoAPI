from rest_framework import serializers
from .models import Suldoc

class SuldocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suldoc
        fields = ('id', 'user_id', 'name', 'comment', 'stars_taste', 'stars_costvalue', 'img_path')