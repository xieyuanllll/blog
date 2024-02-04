from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL , 'NORMAL'),
        (STATUS_DELETE , 'DELETE'),
    )
    name = models.CharField(max_length=50,verbose_name='name')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS,
                                         verbose_name='state'
                                         )
    is_nav = models.BooleanField(default=False,verbose_name='if it is navigation')
    owner = models.ForeignKey(User,verbose_name='author',on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='creation time')

    class Meta:
        verbose_name = verbose_name_plural = 'classify'


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL , '正常'),
        (STATUS_DELETE , '删除'),
    )
    name = models.CharField(max_length=50,verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS,
                                         verbose_name='状态'
                                         )
    owner = models.ForeignKey(User,verbose_name='author',on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='creation time')

    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL , 'NORMAL'),
        (STATUS_DELETE , 'DELETE'),
        (STATUS_DRAFT , 'DRAFT'),
    )
    title = models.CharField(max_length=255,verbose_name='标题')
    desc = models.CharField(max_length=1024,blank=True,verbose_name='摘要')
    content = models.TextField(verbose_name='正文',help_text='正文必须为MarkDown格式')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                          choices=STATUS_ITEMS,
                                          verbose_name='状态')
    category = models.ForeignKey(Category,verbose_name='分类',on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural ='文章'
        ordering = ['-id']
