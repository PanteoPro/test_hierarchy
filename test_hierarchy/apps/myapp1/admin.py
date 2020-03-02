from django.contrib import admin
from .models import Category, Article, Author, Theme, Step, StepForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'cut_body', 'author'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name'


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'body'
    form = StepForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "article":
            kwargs["queryset"] = Theme.objects.filter(pk=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

