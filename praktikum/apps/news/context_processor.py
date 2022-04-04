from apps.news.models import Article, Advertisements, ArticleComment


def get_recent(request):
    last_articles = list(Article.objects.all())[-2:]
    return {'last_article_list': last_articles}


def get_article_category():
    pass


def get_random(request):
    random_article = Article.objects.order_by('?')
    first_article = random_article.first()
    return {'random_article': first_article}


def get_reverse_articles(request):
    reverse_articles = list(Article.objects.order_by('title'))[:3]
    return {'reverse_articles': reverse_articles}


def get_all_articles(request):
    articles = list(Article.objects.all())[:3]
    return {'article_list': articles}


def get_most_viewed(request):
    most_viewed = Article.objects.order_by('views_count')
    return {'most_viewed': most_viewed}


def get_alll_articles(request):
    articles = list(Article.objects.all())[:3]
    return {'article_list_all': articles}


def get_random_add(request):
    random_add = Advertisements.objects.order_by('?')
    first_add = random_add.first()
    return {'random_add': first_add}


def get_comments(request):
    all_comments = ArticleComment.objects.all()
    return {'all_comments': all_comments}



