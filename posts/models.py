from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_symbols


class Post(models.Model):
    # 글의 제목, 내용, 작성일, 마지막 수정일
    title = models.CharField(max_length=50, unique=True, error_messages={'unique': '이미 있는 제목이네요!'})  # 길이 제한있는 문자열 필드
    content = models.TextField(validators=[MinLengthValidator(10, '너무 짧군요! 10자 이상 적어주세요.'), validate_symbols])  # 길이 제한없는 문자열 필드
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)  # auto_now_add : 처음 생성될 때의 시간을 저장
    dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)  # auto_now : 마지막으로 저장될 때의 시간을 저장

    def __str__(self):  # Post 객체를 하나의 문자열로 표현할 수 있다.
        return self.title
