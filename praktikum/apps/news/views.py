from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.views.generic import TemplateView
from regex import F

from apps.news.forms import ArticleCommentForm
from apps.news.models import Article, ArticleComment, ArticleCategory


class ArticleListView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = dict()
        query_parameters = self.request.GET
        search_word = query_parameters.get('search', None)
        print(f'{search_word=}')
        context['article_category_list'] = ArticleCategory.objects.all()
        if search_word:
            context['article_list'] = Article.objects.filter(
                Q(title__icontains=search_word) |
                Q(description__icontains=search_word) |
                Q(categories__title__icontains=search_word)
            )
        else:
            context['article_list'] = list(Article.objects.all())[:3]
        return context


class ArticleSingleView(TemplateView):

    template_name = 'blog-post.html'
    # Article.objects.filter(id=article.pk).update(score=F("score") + 1)

    def get_context_data(self, **kwargs):
        context = dict()
        try:
            article = Article.objects.get(id=kwargs['pk'])

            article.views_count += 1
            article.save()
        except Article.DoesNotExist:
            raise Http404
        context['article'] = article
        return context


def add_comment_view(request, pk):
    if request.method == 'GET':
        response = render(request, 'blog-post.html')
        return response
    elif request.method == 'POST':
        post_request_data = request.POST
        comment_form = ArticleCommentForm(post_request_data)
        if comment_form.is_valid():
            comment = ArticleComment.objects.create(
                text=comment_form.data['text'],
                user_name=comment_form.data['name'],
                user_email=comment_form.data['email'],
                article_id=pk)
            return HttpResponse(content='КОММЕНТАРИЙ УСПЕШНО ДОБАВЛЕН.')
        else:
            return HttpResponse(content=f'Похоже вы неправильно заполнили форму: {comment_form.errors}')
