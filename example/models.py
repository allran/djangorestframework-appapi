from django.db import models
from django.conf import settings

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Blog(BaseModel):
    title = models.CharField(blank=True, null=True, max_length=255, verbose_name='title')
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        to=Author,
        on_delete=models.SET_NULL,
        related_name='author',
        blank=True, null=True,
        verbose_name='作者',
        help_text='作者id'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class UserFavorite(BaseModel):
    """
    用户收藏操作
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='用户',
        help_text='收藏人id'
    )
    blog = models.ForeignKey(
        to=Blog,
        on_delete=models.SET_NULL,
        related_name='blog',
        blank=True, null=True,
        verbose_name='博客',
        help_text='博客id'
    )

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

        # 多个字段作为一个联合唯一索引
        unique_together = ("user", "blog")
        ordering = ['id']

    def __str__(self):
        return '%s. [ %s ] [ %s ]' % (self.pk, self.blog.name, self.user.name)