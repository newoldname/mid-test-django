from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체 안에서 원하는 함수를 작성할 수 있음
    def __str__(self):
        return f"[{self.pk}]{self.title}"