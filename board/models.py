from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class NoticeBoardPost(models.Model):#Board
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=20, null=True)
    content = models.TextField()
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    imgfile = models.ImageField(null=True, upload_to="", blank=True) # 이미지 컬럼 추가
    #deletedAt = models.DateTimeField(null=True)

    def delete(self, *args,**kargs):
        super(NoticeBoardPost,self).delete(*args,**kargs)
    


class Comment(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='댓글작성자')
    commentId = models.ForeignKey(NoticeBoardPost, on_delete=models.CASCADE)
    text = models.TextField()
