# Generated by Django 4.0.2 on 2022-03-30 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('main_text', models.TextField(max_length=2000)),
                ('poster', models.ImageField(upload_to='')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Категория публикаций',
                'verbose_name_plural': 'Категории публикаций',
            },
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('user_name', models.CharField(default='', max_length=100, verbose_name='Имя пользователя')),
                ('user_email', models.EmailField(max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.article')),
            ],
            options={
                'verbose_name': 'Комментарий публикации',
                'verbose_name_plural': 'Комментарии публикаций',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.articlecategory'),
        ),
    ]