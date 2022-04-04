from django.contrib import admin

# Register your models here.
from apps.news.models import Article, ArticleCategory, ArticleComment, Advertisements


@admin.register(Article)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Advertisements)
class AdvertisementsAdmin(admin.ModelAdmin):
    pass