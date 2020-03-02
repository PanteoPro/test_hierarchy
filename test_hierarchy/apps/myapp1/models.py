from django.db import models
from django.forms import ModelForm


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    @property
    def cut_body(self):
        if len(self.body) > 20:
            return f'{self.body[:20]}...'
        return self.body

    def __str__(self):
        return f'{self.title}!r {self.cut_body}'



class Theme(models.Model):
    title = models.CharField(max_length=100)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def count_steps(self):
        return len(self.step_set.all())

    def queryset_steps(self):
        return self.step_set.all()

    def __str__(self):
        return f'{self.article_id}.{self.id} {self.title}'


class Step(models.Model):
    title = models.TextField()
    body = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.title}!r'



class StepForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(StepForm, self).__init__(*args, **kwargs)
        self.fields['theme'].queryset = Theme.objects.filter(article_id=self.instance.article_id)
