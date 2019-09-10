from django.db import models
from rest_framework import serializers


class TasteNoteModel(models.Model):
    user_id = models.CharField(max_length=30)  # 유저 아이디
    name = models.CharField(max_length=100)  # 술 이름
    comment = models.CharField(max_length=200)  # 코멘트
    stars_taste = models.FloatField()  # 맛 평가
    stars_costvalue = models.FloatField()  # 가성비 평가
    img_path = models.CharField(max_length=1000)  # 이미지 경로
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 수정시간

    def __str__(self):
        return self.name


class TasteNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasteNoteModel
        fields = (
            "user_id",
            "name",
            "comment",
            "stars_taste",
            "stars_costvalue",
            "img_path",
            "created_at",
            "updated_at",
        )
