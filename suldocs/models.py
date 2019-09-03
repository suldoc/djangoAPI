from django.db import models

# Create your models here.
class Taste_note(models.Model):
    user_id = models.CharField(max_length=30) # 유저 아이디
    name = models.CharField(max_length=100) # 술 이름
    comment = models.CharField(max_length=200) # 코멘트
    stars_taste = models.FloatField() # 맛 평가
    stars_costvalue = models.FloatField() # 가성비 평가
    img_path = models.CharField(max_length=1000) # 이미지 경로
    create_at = models.DateTimeField(auto_now_add=True) # 작성 시간
    update_at = models.DateTimeField(auto_now=True)  # 수정시간

    def __str__(self):
        return self.name
