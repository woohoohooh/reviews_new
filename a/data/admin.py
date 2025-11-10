import importlib
from django.contrib import admin
from django.utils import timezone
from .abc import SUFFIX_101

def load_model(model_name, suffix):
    try:
        module = importlib.import_module('data.models')
        return getattr(module, f"{model_name}{suffix}")
    except AttributeError:
        raise ImportError(f"Модель {model_name}{suffix} не найдена в data.models")

models = {}
for model_name in ['Tag', 'Author', 'Topic', 'Subtopic', 'Step', 'Comment']:
    key = f"{model_name}{SUFFIX_101}"
    models[key] = load_model(model_name, SUFFIX_101)

globals().update(models)

class CommentInline(admin.TabularInline):
    model = globals()[f'Comment{SUFFIX_101}']
    extra = 0
    fields = ('username', 'text', 'is_published', 'created_date')
    readonly_fields = ('username', 'text', 'created_date')
    ordering = ('-created_date',)
    show_change_link = True

# Админка для Step с комментариями
@admin.register(globals()[f'Step{SUFFIX_101}'])
class StepAdmin(admin.ModelAdmin):
    list_display = ('h1', 'subtitle', 'is_published')
    actions = ['publish_selected']
    list_per_page = 50
    inlines = [CommentInline]

    @admin.action(description="Опубликовать выбранные шаги")
    def publish_selected(self, request, queryset):
        updated_count = queryset.update(is_published=True, published_date=timezone.now())
        self.message_user(request, f"{updated_count} шагов успешно опубликовано.")

@admin.register(globals()[f'Comment{SUFFIX_101}'])
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'step', 'is_published', 'created_date')
    list_filter = ('is_published', 'created_date')
    ordering = ('-created_date',)
    actions = ['approve_comments']

    @admin.action(description="Опубликовать выбранные комментарии")
    def approve_comments(self, request, queryset):
        updated_count = queryset.update(is_published=True, published_date=timezone.now())
        self.message_user(request, f"{updated_count} комментариев опубликовано.")

@admin.register(globals()[f'Author{SUFFIX_101}'])
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('type',)
    search_fields = ('type',)

@admin.register(globals()[f'Topic{SUFFIX_101}'])
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(globals()[f'Subtopic{SUFFIX_101}'])
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic')
    search_fields = ('title', 'topic__title')

@admin.register(globals()[f'Tag{SUFFIX_101}'])
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
