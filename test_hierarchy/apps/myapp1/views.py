from django.shortcuts import render
from .models import Article, Author, Category


def index(request):
    c = Category.objects.get(pk=1)
    articles = c.article_set.all()
    return render(request, 'myapp1/index.html', {
        'articles': articles,
    })


def promo(request, id):
    article = Article.objects.get(pk=id)
    themes = article.theme_set.all()
    steps_d = []
    i = 0
    for t in themes:
        steps_d.append(t.step_set.all())
        i+=1
    steps = []
    for i in steps_d:
        for j in i:
            steps.append(j)
    return render(request, 'myapp1/promo.html', {
        'article': article,
        'themes': themes,
        'steps': steps,
    })