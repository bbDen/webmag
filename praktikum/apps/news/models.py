from django.db import models


# Create your models here.

class ArticleCategory(models.Model):
    """модель для категорий публикации"""
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Категории публикаций'
        verbose_name = 'Категория публикаций'

    def __str__(self):
        return self.title


class Article(models.Model):
    """модель для публикаций"""
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    main_text = models.TextField(max_length=2000)
    poster = models.ImageField()
    created_at = models.DateField(auto_now_add=True)
    categories = models.ForeignKey(to=ArticleCategory, on_delete=models.CASCADE)
    views_count = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    """Модель для коментариев публикации"""

    text = models.TextField(verbose_name='Текст')
    user_name = models.CharField(max_length=100, verbose_name='Имя пользователя', default='')
    user_email = models.EmailField(null=True)
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE,
                                related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Комментарии публикаций'
        verbose_name = 'Комментарий публикации'

    def __str__(self):
        return f'Комментарий для публикации с id:{self.article_id}'


class Advertisements(models.Model):

    poster = models.ImageField()
