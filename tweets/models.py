from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    # Userと紐付けするためのカラム
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    # コメントを追加するためのカラム
    text = models.TextField(blank=True, null=False)
    # 投稿日を持つためのカラム
    created_at = models.DateTimeField(auto_now_add=True, blank=True)