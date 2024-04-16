from django.db import models
from django.utils import timezone

# Create your models here.
class NoticeBoardPost(models.Model):#Board
   
    title = models.CharField(max_length=20, null=True)
    content = models.TextField()
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    imgfile = models.ImageField(null=True, upload_to="", blank=True) # 이미지 컬럼 추가
    #deletedAt = models.DateTimeField(null=True)
    


class Comment(models.Model):
    commentId = models.ForeignKey(NoticeBoardPost, on_delete=models.CASCADE)
    text = models.TextField()
