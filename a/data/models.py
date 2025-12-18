import os
import re
from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify
from django.urls import reverse
from django.core.exceptions import ValidationError
from .abc import SUFFIX

STEP_VERBOSE_NAME_001 = "а — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_001 = "a — модули"
TOPIC_VERBOSE_NAME_001 = "а — темы"
AUTHOR_VERBOSE_NAME_001 = "а — авторы"
TAGS_VERBOSE_NAME_001 = "а — теги"
COMMENTS_VERBOSE_NAME_001 = "а — комменты"

STEP_VERBOSE_NAME_002 = "bank — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_002 = "bank — модули"
TOPIC_VERBOSE_NAME_002 = "bank — темы"
AUTHOR_VERBOSE_NAME_002 = "bank — авторы"
TAGS_VERBOSE_NAME_002 = "bank — теги"
COMMENTS_VERBOSE_NAME_002 = "bank — комменты"

STEP_VERBOSE_NAME_003 = "health — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_003 = "health — модули"
TOPIC_VERBOSE_NAME_003 = "health — темы"
AUTHOR_VERBOSE_NAME_003 = "health — авторы"
TAGS_VERBOSE_NAME_003 = "health — теги"
COMMENTS_VERBOSE_NAME_003 = "health — комменты"

STEP_VERBOSE_NAME_004 = "auto — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_004 = "auto — модули"
TOPIC_VERBOSE_NAME_004 = "auto — темы"
AUTHOR_VERBOSE_NAME_004 = "auto — авторы"
TAGS_VERBOSE_NAME_004 = "auto — теги"
COMMENTS_VERBOSE_NAME_004 = "auto — комменты"

STEP_VERBOSE_NAME_005 = "hightech — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_005 = "hightech — модули"
TOPIC_VERBOSE_NAME_005 = "hightech — темы"
AUTHOR_VERBOSE_NAME_005 = "hightech — авторы"
TAGS_VERBOSE_NAME_005 = "hightech — теги"
COMMENTS_VERBOSE_NAME_005 = "hightech — комменты"

STEP_VERBOSE_NAME_006 = "lawyer — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_006 = "lawyer — модули"
TOPIC_VERBOSE_NAME_006 = "lawyer — темы"
AUTHOR_VERBOSE_NAME_006 = "lawyer — авторы"
TAGS_VERBOSE_NAME_006 = "lawyer — теги"
COMMENTS_VERBOSE_NAME_006 = "lawyer — комменты"

STEP_VERBOSE_NAME_007 = "doker — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_007 = "doker — модули"
TOPIC_VERBOSE_NAME_007 = "doker — темы"
AUTHOR_VERBOSE_NAME_007 = "doker — авторы"
TAGS_VERBOSE_NAME_007 = "doker — теги"
COMMENTS_VERBOSE_NAME_007 = "doker — комменты"

STEP_VERBOSE_NAME_008 = "psycho — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_008 = "psycho — модули"
TOPIC_VERBOSE_NAME_008 = "psycho — темы"
AUTHOR_VERBOSE_NAME_008 = "psycho — авторы"
TAGS_VERBOSE_NAME_008 = "psycho — теги"
COMMENTS_VERBOSE_NAME_008 = "psycho — комменты"

STEP_VERBOSE_NAME_009 = "homeapps — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_009 = "homeapps — модули"
TOPIC_VERBOSE_NAME_009 = "homeapps — темы"
AUTHOR_VERBOSE_NAME_009 = "homeapps — авторы"
TAGS_VERBOSE_NAME_009 = "homeapps — теги"
COMMENTS_VERBOSE_NAME_009 = "homeapps — комменты"

STEP_VERBOSE_NAME_010 = "job — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_010 = "job — модули"
TOPIC_VERBOSE_NAME_010 = "job — темы"
AUTHOR_VERBOSE_NAME_010 = "job — авторы"
TAGS_VERBOSE_NAME_010 = "job — теги"
COMMENTS_VERBOSE_NAME_010 = "job — комменты"

STEP_VERBOSE_NAME_011 = "garden — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_011 = "garden — модули"
TOPIC_VERBOSE_NAME_011 = "garden — темы"
AUTHOR_VERBOSE_NAME_011 = "garden — авторы"
TAGS_VERBOSE_NAME_011 = "garden — теги"
COMMENTS_VERBOSE_NAME_011 = "garden — комменты"

STEP_VERBOSE_NAME_012 = "war — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_012 = "war — модули"
TOPIC_VERBOSE_NAME_012 = "war — темы"
AUTHOR_VERBOSE_NAME_012 = "war — авторы"
TAGS_VERBOSE_NAME_012 = "war — теги"
COMMENTS_VERBOSE_NAME_012 = "war — комменты"

STEP_VERBOSE_NAME_013 = "animals — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_013 = "animals — модули"
TOPIC_VERBOSE_NAME_013 = "animals — темы"
AUTHOR_VERBOSE_NAME_013 = "animals — авторы"
TAGS_VERBOSE_NAME_013 = "animals — теги"
COMMENTS_VERBOSE_NAME_013 = "animals — комменты"

STEP_VERBOSE_NAME_014 = "courses — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_014 = "courses — модули"
TOPIC_VERBOSE_NAME_014 = "courses — темы"
AUTHOR_VERBOSE_NAME_014 = "courses — авторы"
TAGS_VERBOSE_NAME_014 = "courses — теги"
COMMENTS_VERBOSE_NAME_014 = "courses — комменты"

STEP_VERBOSE_NAME_015 = "food — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_015 = "food — модули"
TOPIC_VERBOSE_NAME_015 = "food — темы"
AUTHOR_VERBOSE_NAME_015 = "food — авторы"
TAGS_VERBOSE_NAME_015 = "food — теги"
COMMENTS_VERBOSE_NAME_015 = "food — комменты"

STEP_VERBOSE_NAME_016 = "mystic — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_016 = "mystic — модули"
TOPIC_VERBOSE_NAME_016 = "mystic — темы"
AUTHOR_VERBOSE_NAME_016 = "mystic — авторы"
TAGS_VERBOSE_NAME_016 = "mystic — теги"
COMMENTS_VERBOSE_NAME_016 = "mystic — комменты"

STEP_VERBOSE_NAME_017 = "realty — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_017 = "realty — модули"
TOPIC_VERBOSE_NAME_017 = "realty — темы"
AUTHOR_VERBOSE_NAME_017 = "realty — авторы"
TAGS_VERBOSE_NAME_017 = "realty — теги"
COMMENTS_VERBOSE_NAME_017 = "realty — комменты"

STEP_VERBOSE_NAME_018 = "build — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_018 = "build — модули"
TOPIC_VERBOSE_NAME_018 = "build — темы"
AUTHOR_VERBOSE_NAME_018 = "build — авторы"
TAGS_VERBOSE_NAME_018 = "build — теги"
COMMENTS_VERBOSE_NAME_018 = "build — комменты"

STEP_VERBOSE_NAME_101 = "reviews — ТРЕКИ"
SUBTOPIC_VERBOSE_NAME_101 = "reviews — модули"
TOPIC_VERBOSE_NAME_101 = "reviews — темы"
AUTHOR_VERBOSE_NAME_101 = "reviews — авторы"
TAGS_VERBOSE_NAME_101 = "reviews — теги"
COMMENTS_VERBOSE_NAME_101 = "reviews — комменты"

def custom_slugify(value):
    return slugify(value, allow_unicode=True)

def get_unique_file_path(instance, filename):
    base_path = f'{SUFFIX}/{now().year}/{now().month}/'
    full_path = os.path.join(base_path, filename)
    file_root, file_ext = os.path.splitext(filename)
    counter = 1
    while os.path.exists(full_path):
        new_filename = f"{file_root}-{counter}{file_ext}"
        full_path = os.path.join(base_path, new_filename)
        counter += 1
    return full_path

def get_upload_to(instance, filename):
    base_path = f'{SUFFIX}/{now().year}/{now().month}/'
    file_name = instance.image_file_name or os.path.splitext(filename)[0]
    file_ext = os.path.splitext(filename)[1]
    return os.path.join(base_path, f"{slugify(file_name, allow_unicode=True)}{file_ext}")




# 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001



class Author001(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_001
        verbose_name_plural = AUTHOR_VERBOSE_NAME_001
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic001(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_001
        verbose_name_plural = TOPIC_VERBOSE_NAME_001
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic001(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic001, related_name='subtopics001', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_001
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_001
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])

class Tag001(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")
    class Meta:
        db_table = "tag001"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_001
        verbose_name_plural = TAGS_VERBOSE_NAME_001
        ordering = ['name']
    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)
            base_slug = self.slug
            counter = 1
            while Tag001.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Step001(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic001, related_name='steps001', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag001, related_name="steps001", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author001, related_name='steps001', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_001
        verbose_name_plural = STEP_VERBOSE_NAME_001
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment001(models.Model):
    step = models.ForeignKey('Step001', on_delete=models.CASCADE, related_name='comments001', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_001
        verbose_name_plural = COMMENTS_VERBOSE_NAME_001
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002


# 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002 002



#
# class Author002(models.Model):
#     type = models.CharField(max_length=100)
#     title = models.CharField(max_length=150, verbose_name="Заголовок title")
#     keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
#     seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
#     description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
#     h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
#     image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
#     image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
#     is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
#     slug = models.SlugField(unique=True, max_length=150, allow_unicode=True, blank=True)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title, allow_unicode=True)
#         if self.image and not self.image_file_name:
#             self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
#         super().save(*args, **kwargs)
#
#     def get_absolute_url(self):
#         return reverse('author_detail', args=[self.slug])
#
#     class Meta:
#         verbose_name = AUTHOR_VERBOSE_NAME_002
#         verbose_name_plural = AUTHOR_VERBOSE_NAME_002
#         indexes = [
#             models.Index(fields=['is_published']),
#             models.Index(fields=['slug']),
#         ]
#
#     def __str__(self):
#         return self.type
#
#
# class Topic002(models.Model):
#     slug = models.SlugField(unique=True, allow_unicode=True, max_length=150, blank=True)
#     title = models.CharField(max_length=150)
#     keywords = models.CharField(max_length=250, blank=True, null=True)
#     seo_description = models.CharField(max_length=350, blank=True, null=True)
#     description = models.TextField(blank=True, max_length=11000)
#     h1 = models.CharField(max_length=150, blank=True, null=True)
#     image = models.ImageField(upload_to=get_upload_to, blank=True, null=True)
#     image_file_name = models.CharField(max_length=150, blank=True, null=True)
#     image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = custom_slugify(self.title)
#         if self.image and not self.image_file_name:
#             self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
#         super().save(*args, **kwargs)
#
#     def image_url(self):
#         if self.image:
#             return self.image.url
#         return ''
#
#     def get_absolute_url(self):
#         return reverse('subtopic_list', args=[self.slug])
#
#     class Meta:
#         verbose_name = TOPIC_VERBOSE_NAME_002
#         verbose_name_plural = TOPIC_VERBOSE_NAME_002
#         indexes = [
#             models.Index(fields=['slug']),
#         ]
#
#     def __str__(self):
#         return self.title
#
#
# class Subtopic002(models.Model):
#     slug = models.SlugField(unique=True, allow_unicode=True, max_length=150, blank=True)
#     title = models.CharField(max_length=150)
#     keywords = models.CharField(max_length=250, blank=True, null=True)
#     seo_description = models.CharField(max_length=350, blank=True, null=True)
#     description = models.TextField(blank=True, max_length=11000)
#     h1 = models.CharField(max_length=150, blank=True, null=True)
#     image = models.ImageField(upload_to=get_upload_to, blank=True, null=True)
#     image_file_name = models.CharField(max_length=150, blank=True, null=True)
#     image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True)
#
#     topic = models.ForeignKey(
#         Topic002, related_name='subtopics002',
#         on_delete=models.CASCADE, null=True, blank=True
#     )
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = custom_slugify(self.title)
#         if self.image and not self.image_file_name:
#             self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
#         super().save(*args, **kwargs)
#
#     def get_absolute_url(self):
#         return reverse('subtopic_list', args=[self.slug])
#
#     class Meta:
#         verbose_name = SUBTOPIC_VERBOSE_NAME_002
#         verbose_name_plural = SUBTOPIC_VERBOSE_NAME_002
#         indexes = [
#             models.Index(fields=['slug']),
#         ]
#
#     def __str__(self):
#         return self.title
#
#
# class Tag002(models.Model):
#     name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
#     slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг", blank=True)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         db_table = "tag002"
#         verbose_name = TAGS_VERBOSE_NAME_002
#         verbose_name_plural = TAGS_VERBOSE_NAME_002
#         ordering = ['name']
#         indexes = [
#             models.Index(fields=['slug']),
#             models.Index(fields=['name']),
#         ]
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name.lower(), allow_unicode=True)
#             base_slug = self.slug
#             counter = 1
#             while Tag002.objects.filter(slug=self.slug).exists():
#                 self.slug = f"{base_slug}-{counter}"
#                 counter += 1
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.name
#
#
# class Type002(models.Model):
#     name = models.CharField(max_length=100, unique=True, verbose_name="Название типа")
#     slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг", blank=True)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = TAGS_VERBOSE_NAME_002
#         verbose_name_plural = TAGS_VERBOSE_NAME_002
#         ordering = ['name']
#         indexes = [
#             models.Index(fields=['slug']),
#             models.Index(fields=['name']),
#         ]
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name.lower(), allow_unicode=True)
#             base_slug = self.slug
#             counter = 1
#             while Type002.objects.filter(slug=self.slug).exists():
#                 self.slug = f"{base_slug}-{counter}"
#                 counter += 1
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.name
#
# LANG_CHOICES = [
#     ('en', 'English'),
#     ('ru', 'Russian'),
#     ('es', 'Spanish'),
#     ('zh', 'Chinese'),
# ]
# class Step002(models.Model):
#     language = models.CharField(max_length=5, choices=LANG_CHOICES, default='en', db_index=True)
#     description = models.TextField(blank=True, max_length=11000)
#     title = models.CharField(max_length=150)
#     h1 = models.CharField(max_length=150)
#     keyword = models.CharField(max_length=150, blank=True, null=True, unique=True)
#     keywords = models.CharField(max_length=250, blank=True, null=True)
#     image = models.ImageField(upload_to=get_upload_to, blank=True, null=True)
#     image_file_name = models.CharField(max_length=150, blank=True, null=True)
#     image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True)
#     subtopic = models.ForeignKey(Subtopic002, related_name='steps002', on_delete=models.CASCADE, db_index=True)
#     tags = models.ManyToManyField(Tag002, related_name="steps002", blank=True)
#     author_type = models.ForeignKey(Author002, related_name='steps002', on_delete=models.CASCADE)
#     seo_description = models.CharField(max_length=350, blank=True, null=True)
#     slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, blank=True)
#     is_published = models.BooleanField(default=False, db_index=True)
#     published_date = models.DateTimeField(null=True, blank=True, db_index=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     views = models.PositiveIntegerField(default=0, db_index=True)
#
#     def increment_views(self):
#         self.views += 1
#         self.save(update_fields=['views'])
#
#     class Meta:
#         unique_together = ('slug', 'language')
#         indexes = [
#             models.Index(fields=['is_published', 'published_date']),
#         ]
#         verbose_name = STEP_VERBOSE_NAME_002
#         verbose_name_plural = STEP_VERBOSE_NAME_002
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('step_detail', args=[self.slug])
#
#     @property
#     def formatted_updated_date(self):
#         return self.updated_at.strftime('%d.%m.%Y')
#
#     def clean(self):
#         if self.slug and len(self.slug) > 150:
#             raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
#         if self.seo_description and len(self.seo_description) > 350:
#             raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
#         if self.keyword and len(self.keyword) > 150:
#             raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
#         if self.description and len(self.description) > 11000:
#             raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
#         if self.h1 and len(self.h1) > 150:
#             raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
#         if self.image_file_name and len(self.image_file_name) > 150:
#             raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
#
#     def save(self, *args, **kwargs):
#         self.full_clean()
#         if self.is_published and not self.published_date:
#             self.published_date = now()
#         if not self.slug:
#             clean_title = self.title.strip().replace('\r', '').replace('\n', '')
#             self.slug = slugify(clean_title, allow_unicode=True)
#         if self.image and not self.image_file_name:
#             self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
#         super().save(*args, **kwargs)
#
# class Comment002(models.Model):
#     step = models.ForeignKey('Step002', on_delete=models.CASCADE, related_name='comments002', db_index=True, verbose_name="Шаг")
#     username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
#     text = models.TextField(verbose_name="Текст комментария")
#     is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
#     published_at = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
#     updated_at = models.DateTimeField(auto_now=True)
#     parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
#     is_spam = models.BooleanField(default=False, db_index=True)
#
#     def approve(self):
#         self.is_published = True
#         self.published_at = timezone.now()
#         self.save(update_fields=['is_published', 'published_at'])
#
#     def save(self, *args, **kwargs):
#         if self.is_published and not self.published_at:
#             self.published_at = timezone.now()
#         elif not self.is_published:
#             self.published_at = None
#         super().save(*args, **kwargs)
#
#     class Meta:
#         indexes = [
#             models.Index(fields=['step', 'is_published', 'published_at']),
#         ]
#         verbose_name = COMMENTS_VERBOSE_NAME_002
#         verbose_name_plural = COMMENTS_VERBOSE_NAME_002
#
#     def __str__(self):
#         return f"Комментарий от {self.username} ({self.created_at:%d.%m.%Y})"
#
#     @property
#     def formatted_created_date(self):
#         return self.created_at.strftime('%d.%m.%Y')


    # author_expert = models.ForeignKey('Author002', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Автор экспертного мнения")
    # topic = models.ManyToManyField('Topic002', blank=True, verbose_name="Категория")
    # subtopic = models.ManyToManyField('Subtopic002', blank=True, verbose_name="Рынок")
    # type = models.ManyToManyField('Type002', blank=True, verbose_name="Тип")

from django.urls import reverse
from django.utils.text import slugify


from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# ================== СПРАВОЧНИКИ ==================

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, allow_unicode=True)
    description = models.TextField(blank=True, default='')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, allow_unicode=True)
    description = models.TextField(blank=True, default='')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class InvestmentType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, allow_unicode=True)
    description = models.TextField(blank=True, default='')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, default='')
    popularity = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AIAnalyzeYear(models.Model):
    year = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.year)


# ================== ЭКСПЕРТ ==================

class Expert(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)

    position = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)

    bio = models.TextField(blank=True, default='')

    link_site = models.URLField(blank=True, null=True)
    link_linkedin = models.URLField(blank=True, null=True)
    link_x = models.URLField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# ================== ОСНОВНАЯ МОДЕЛЬ ==================

class Project002(models.Model):
    LANG_CHOICES = [
        ('en', 'English'),
        ('ru', 'Russian'),
        ('es', 'Espanol'),
        ('zh', 'China'),
        ('ar', 'Arr'),
    ]

    language = models.CharField(
        'Язык',
        max_length=5,
        choices=LANG_CHOICES,
        default='en',
        db_index=True
    )

    status = models.CharField(max_length=1000, null=True, blank=True)
    project_name = models.CharField(max_length=500, null=True, blank=True)
    project_subname = models.CharField(max_length=500, null=True, blank=True)

    slug = models.SlugField(
        allow_unicode=True,
        max_length=500,
        blank=True,
        null=True
    )

    link_site = models.URLField(null=True, blank=True)
    published = models.BooleanField(default=False)

    description_short = models.TextField(blank=True, default='')
    description_full = models.TextField(blank=True, default='')
    description_seo = models.TextField(blank=True, default='')

    title = models.CharField(max_length=1000, null=True, blank=True)
    alt_brands = models.CharField(max_length=500, null=True, blank=True)
    keywords = models.CharField(max_length=500, null=True, blank=True)

    plus_minus = models.CharField(max_length=10000, null=True, blank=True)
    criteries = models.CharField(max_length=1000, null=True, blank=True)

    description_team_short = models.TextField(blank=True, default='')
    description_team_full = models.TextField(blank=True, default='')

    ai_summarize = models.TextField(blank=True, default='')
    current_activity = models.TextField(blank=True, default='')

    ticker = models.CharField(max_length=500, null=True, blank=True)

    # ---------- ЭКСПЕРТНОЕ МНЕНИЕ ----------
    expert_opinion = models.TextField(blank=True, default='')
    expert_recommend = models.BooleanField(default=False)

    expert_author = models.ForeignKey(
        Expert,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='projects'
    )

    started_at = models.DateField(null=True, blank=True)
    started_at_tooltip = models.TextField(blank=True, default='')

    domain_registered = models.TextField(blank=True, default='')
    domain_registered_tooltip = models.TextField(blank=True, default='')

    location = models.CharField(max_length=1000, null=True, blank=True)

    RISK_CHOICES = [
        ("super_low", "Super Low"),
        ("low", "Low"),
        ("average", "Average"),
        ("high", "High"),
        ("super_high", "Super High"),
    ]

    pays_or_not = models.CharField(max_length=1000, null=True, blank=True)
    risk = models.CharField(max_length=50, choices=RISK_CHOICES, null=True, blank=True)
    risk_tooltip = models.TextField(blank=True, default='')

    RATING_CHOICES = [(str(i), str(i)) for i in range(6)] + [("5_plus", "5+")]
    our_rating = models.CharField(max_length=10, choices=RATING_CHOICES, null=True, blank=True)
    our_rating_tooltip = models.TextField(blank=True, default='')

    our_advice = models.TextField(blank=True, default='')
    our_advice_tooltip = models.TextField(blank=True, default='')
    our_opinion = models.TextField(blank=True, default='')

    type_of_payments = models.TextField(blank=True, default='')
    currencies_payment = models.CharField(max_length=500, null=True, blank=True)

    results_digits = models.CharField(max_length=500, null=True, blank=True)
    results_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    results_period = models.DateField(null=True, blank=True)

    min_investment = models.IntegerField(null=True, blank=True)
    max_investment = models.IntegerField(null=True, blank=True)

    investors = models.IntegerField(null=True, blank=True)
    investors_tooltip = models.TextField(blank=True, default='')

    competitors = models.CharField(max_length=1000, null=True, blank=True)
    investing_type = models.CharField(max_length=500, null=True, blank=True)
    dividends_type = models.CharField(max_length=500, null=True, blank=True)

    # ---------- ССЫЛКИ ----------
    link_github = models.URLField(null=True, blank=True)
    link_register = models.URLField(null=True, blank=True)
    link_plans = models.URLField(null=True, blank=True)
    link_conditions = models.URLField(null=True, blank=True)
    link_terms_fees = models.URLField(null=True, blank=True)

    link_tg_channel = models.URLField(null=True, blank=True)
    link_tg_group = models.URLField(null=True, blank=True)
    link_youtube = models.URLField(null=True, blank=True)
    link_facebook = models.URLField(null=True, blank=True)
    link_x = models.URLField(null=True, blank=True)
    link_another = models.URLField(null=True, blank=True)

    link_whitepaper = models.URLField(null=True, blank=True)
    link_news = models.URLField(null=True, blank=True)

    phones = models.CharField(max_length=500, null=True, blank=True)

    link_independent_stats = models.URLField(null=True, blank=True)
    link_independent_stats_tooltip = models.URLField(max_length=500, null=True, blank=True)
    link_independent_reviews = models.URLField(null=True, blank=True)
    link_independent_reviews_tooltip = models.URLField(max_length=500, null=True, blank=True)

    # ---------- ИЗОБРАЖЕНИЯ ----------
    img_main_page = models.ImageField(upload_to='projects/logos/', blank=True)
    img_logo = models.ImageField(upload_to='projects/logos/', blank=True)
    img_cover = models.ImageField(upload_to='projects/cover/', blank=True)
    img_cover_description = models.TextField(blank=True, default='')
    img_cover_filename = models.CharField(max_length=500, null=True, blank=True)

    # ---------- ФЛАГИ ----------
    our_project = models.BooleanField(default=False)
    top = models.BooleanField(default=False)
    pro = models.BooleanField(default=False)

    last_payment_date = models.DateField(null=True, blank=True)

    average_income_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    average_income_digits = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_income_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_income_digits = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    all_time_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    all_time_digits = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    our_deposit_all_time = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    pool_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pool_digits = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    max_drawdown = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    search_phases = models.CharField(max_length=500, null=True, blank=True)

    published_at = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ---------- СВЯЗИ ----------
    categories = models.ManyToManyField(Category, blank=True, related_name='projects')
    markets = models.ManyToManyField(Market, blank=True, related_name='projects')
    investment_types = models.ManyToManyField(InvestmentType, blank=True, related_name='projects')
    tags = models.ManyToManyField(Tag, blank=True, related_name='projects')
    ai_analyze_yearly = models.ManyToManyField(AIAnalyzeYear, blank=True, related_name='projects')

    related_posts = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='related_to'
    )

    class Meta:
        ordering = ['-published_at', '-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['language', 'slug'],
                name='unique_project_slug_per_language'
            )
        ]

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug, 'lang': self.language})

    def save(self, *args, **kwargs):
        if not self.slug and self.project_name:
            self.slug = slugify(self.project_name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.project_name or 'Без названия'} ({self.language})"


# ================== КОММЕНТАРИИ ==================

class ProjectComment(models.Model):
    project = models.ForeignKey(Project002, on_delete=models.CASCADE, related_name='comments')

    author_name = models.CharField(max_length=255)
    author_email = models.EmailField(blank=True, null=True)

    comment = models.TextField()
    recommend = models.BooleanField(default=False)

    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.author_name}: {self.comment[:40]}"


#
# class CommentInvestProject002(models.Model):
#     project = models.ForeignKey('InvestProject002', on_delete=models.CASCADE, related_name='comments_invest', verbose_name="Проект")
#     name = models.CharField(max_length=300, default='Anonymous')
#     content = models.TextField()
#     is_positive = models.BooleanField(default=True)
#     published = models.BooleanField('Опубликовано', default=False)
#     rating = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Лайки")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
#     is_spam = models.BooleanField(default=False, db_index=True)
#
#     def approve(self):
#         self.published = True
#         self.save(update_fields=['published'])
#
#     class Meta:
#         indexes = [
#             models.Index(fields=['project', 'published', 'created_at']),
#             models.Index(fields=['rating']),
#         ]
#         verbose_name = "Комментарий проекта"
#         verbose_name_plural = "Комментарии проектов"
#
#     def __str__(self):
#         return f"{self.name} ({self.created_at:%d.%m.%Y})"


# 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003 003



class Author003(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_003
        verbose_name_plural = AUTHOR_VERBOSE_NAME_003
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic003(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_003
        verbose_name_plural = TOPIC_VERBOSE_NAME_003
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic003(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic003, related_name='subtopics003', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_003
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_003
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag003(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag003"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_003
        verbose_name_plural = TAGS_VERBOSE_NAME_003
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag003.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step003(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic003, related_name='steps003', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag003, related_name="steps003", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author003, related_name='steps003', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_003
        verbose_name_plural = STEP_VERBOSE_NAME_003
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment003(models.Model):
    step = models.ForeignKey('Step003', on_delete=models.CASCADE, related_name='comments003', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_003
        verbose_name_plural = COMMENTS_VERBOSE_NAME_003
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004 004



class Author004(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_004
        verbose_name_plural = AUTHOR_VERBOSE_NAME_004
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic004(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_004
        verbose_name_plural = TOPIC_VERBOSE_NAME_004
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic004(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic004, related_name='subtopics004', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_004
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_004
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag004(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag004"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_004
        verbose_name_plural = TAGS_VERBOSE_NAME_004
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag004.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step004(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic004, related_name='steps004', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag004, related_name="steps004", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author004, related_name='steps004', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_004
        verbose_name_plural = STEP_VERBOSE_NAME_004
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment004(models.Model):
    step = models.ForeignKey('Step004', on_delete=models.CASCADE, related_name='comments004', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_004
        verbose_name_plural = COMMENTS_VERBOSE_NAME_004
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005 005



class Author005(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_005
        verbose_name_plural = AUTHOR_VERBOSE_NAME_005
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic005(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_005
        verbose_name_plural = TOPIC_VERBOSE_NAME_005
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic005(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic005, related_name='subtopics005', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_005
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_005
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag005(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag005"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_005
        verbose_name_plural = TAGS_VERBOSE_NAME_005
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag005.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step005(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic005, related_name='steps005', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag005, related_name="steps005", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author005, related_name='steps005', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_005
        verbose_name_plural = STEP_VERBOSE_NAME_005
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment005(models.Model):
    step = models.ForeignKey('Step005', on_delete=models.CASCADE, related_name='comments005', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_005
        verbose_name_plural = COMMENTS_VERBOSE_NAME_005
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006 006

class Author006(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_006
        verbose_name_plural = AUTHOR_VERBOSE_NAME_006
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic006(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_006
        verbose_name_plural = TOPIC_VERBOSE_NAME_006
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic006(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic006, related_name='subtopics006', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_006
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_006
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag006(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag006"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_006
        verbose_name_plural = TAGS_VERBOSE_NAME_006
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag006.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step006(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic006, related_name='steps006', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag006, related_name="steps006", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author006, related_name='steps006', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_006
        verbose_name_plural = STEP_VERBOSE_NAME_006
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment006(models.Model):
    step = models.ForeignKey('Step006', on_delete=models.CASCADE, related_name='comments006', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_006
        verbose_name_plural = COMMENTS_VERBOSE_NAME_006
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007 007

class Author007(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_007
        verbose_name_plural = AUTHOR_VERBOSE_NAME_007
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic007(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_007
        verbose_name_plural = TOPIC_VERBOSE_NAME_007
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic007(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic007, related_name='subtopics007', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_007
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_007
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag007(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag007"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_007
        verbose_name_plural = TAGS_VERBOSE_NAME_007
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag007.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step007(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic007, related_name='steps007', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag007, related_name="steps007", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author007, related_name='steps007', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_007
        verbose_name_plural = STEP_VERBOSE_NAME_007
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment007(models.Model):
    step = models.ForeignKey('Step007', on_delete=models.CASCADE, related_name='comments007', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_007
        verbose_name_plural = COMMENTS_VERBOSE_NAME_007
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008 008

class Author008(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_008
        verbose_name_plural = AUTHOR_VERBOSE_NAME_008
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic008(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_008
        verbose_name_plural = TOPIC_VERBOSE_NAME_008
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic008(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic008, related_name='subtopics008', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_008
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_008
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag008(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag008"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_008
        verbose_name_plural = TAGS_VERBOSE_NAME_008
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag008.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step008(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic008, related_name='steps008', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag008, related_name="steps008", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author008, related_name='steps008', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_008
        verbose_name_plural = STEP_VERBOSE_NAME_008
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment008(models.Model):
    step = models.ForeignKey('Step008', on_delete=models.CASCADE, related_name='comments008', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_008
        verbose_name_plural = COMMENTS_VERBOSE_NAME_008
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009 009

class Author009(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_009
        verbose_name_plural = AUTHOR_VERBOSE_NAME_009
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic009(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_009
        verbose_name_plural = TOPIC_VERBOSE_NAME_009
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic009(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic009, related_name='subtopics009', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_009
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_009
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag009(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag009"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_009
        verbose_name_plural = TAGS_VERBOSE_NAME_009
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag009.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step009(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic009, related_name='steps009', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag009, related_name="steps009", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author009, related_name='steps009', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_009
        verbose_name_plural = STEP_VERBOSE_NAME_009
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment009(models.Model):
    step = models.ForeignKey('Step009', on_delete=models.CASCADE, related_name='comments009', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_009
        verbose_name_plural = COMMENTS_VERBOSE_NAME_009
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010 010

class Author010(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_010
        verbose_name_plural = AUTHOR_VERBOSE_NAME_010
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic010(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_010
        verbose_name_plural = TOPIC_VERBOSE_NAME_010
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic010(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic010, related_name='subtopics010', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_010
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_010
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag010(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag010"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_010
        verbose_name_plural = TAGS_VERBOSE_NAME_010
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag010.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step010(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic010, related_name='steps010', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag010, related_name="steps010", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author010, related_name='steps010', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_010
        verbose_name_plural = STEP_VERBOSE_NAME_010
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment010(models.Model):
    step = models.ForeignKey('Step010', on_delete=models.CASCADE, related_name='comments010', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_010
        verbose_name_plural = COMMENTS_VERBOSE_NAME_010
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011

class Author011(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_011
        verbose_name_plural = AUTHOR_VERBOSE_NAME_011
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic011(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_011
        verbose_name_plural = TOPIC_VERBOSE_NAME_011
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic011(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic011, related_name='subtopics011', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_011
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_011
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag011(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag011"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_011
        verbose_name_plural = TAGS_VERBOSE_NAME_011
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag011.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step011(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic011, related_name='steps011', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag011, related_name="steps011", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author011, related_name='steps011', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_011
        verbose_name_plural = STEP_VERBOSE_NAME_011
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment011(models.Model):
    step = models.ForeignKey('Step011', on_delete=models.CASCADE, related_name='comments011', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_011
        verbose_name_plural = COMMENTS_VERBOSE_NAME_011
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012 012

class Author012(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_012
        verbose_name_plural = AUTHOR_VERBOSE_NAME_012
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic012(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_012
        verbose_name_plural = TOPIC_VERBOSE_NAME_012
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic012(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic012, related_name='subtopics012', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_012
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_012
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag012(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag012"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_012
        verbose_name_plural = TAGS_VERBOSE_NAME_012
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag012.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step012(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic012, related_name='steps012', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag012, related_name="steps012", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author012, related_name='steps012', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_012
        verbose_name_plural = STEP_VERBOSE_NAME_012
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment012(models.Model):
    step = models.ForeignKey('Step012', on_delete=models.CASCADE, related_name='comments012', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_012
        verbose_name_plural = COMMENTS_VERBOSE_NAME_012
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013 013

class Author013(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_013
        verbose_name_plural = AUTHOR_VERBOSE_NAME_013
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic013(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_013
        verbose_name_plural = TOPIC_VERBOSE_NAME_013
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic013(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic013, related_name='subtopics013', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_013
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_013
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag013(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag013"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_013
        verbose_name_plural = TAGS_VERBOSE_NAME_013
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag013.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step013(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic013, related_name='steps013', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag013, related_name="steps013", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author013, related_name='steps013', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_013
        verbose_name_plural = STEP_VERBOSE_NAME_013
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment013(models.Model):
    step = models.ForeignKey('Step013', on_delete=models.CASCADE, related_name='comments013', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_013
        verbose_name_plural = COMMENTS_VERBOSE_NAME_013
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014 014

class Author014(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_014
        verbose_name_plural = AUTHOR_VERBOSE_NAME_014
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic014(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_014
        verbose_name_plural = TOPIC_VERBOSE_NAME_014
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic014(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic014, related_name='subtopics014', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_014
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_014
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag014(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag014"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_014
        verbose_name_plural = TAGS_VERBOSE_NAME_014
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag014.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step014(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic014, related_name='steps014', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag014, related_name="steps014", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author014, related_name='steps014', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_014
        verbose_name_plural = STEP_VERBOSE_NAME_014
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment014(models.Model):
    step = models.ForeignKey('Step014', on_delete=models.CASCADE, related_name='comments014', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_014
        verbose_name_plural = COMMENTS_VERBOSE_NAME_014
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015 015

class Author015(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_015
        verbose_name_plural = AUTHOR_VERBOSE_NAME_015
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic015(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_015
        verbose_name_plural = TOPIC_VERBOSE_NAME_015
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic015(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic015, related_name='subtopics015', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_015
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_015
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag015(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag015"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_015
        verbose_name_plural = TAGS_VERBOSE_NAME_015
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag015.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step015(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic015, related_name='steps015', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag015, related_name="steps015", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author015, related_name='steps015', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_015
        verbose_name_plural = STEP_VERBOSE_NAME_015
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment015(models.Model):
    step = models.ForeignKey('Step015', on_delete=models.CASCADE, related_name='comments015', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_015
        verbose_name_plural = COMMENTS_VERBOSE_NAME_015
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016 016

class Author016(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_016
        verbose_name_plural = AUTHOR_VERBOSE_NAME_016
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic016(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_016
        verbose_name_plural = TOPIC_VERBOSE_NAME_016
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic016(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic016, related_name='subtopics016', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_016
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_016
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag016(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag016"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_016
        verbose_name_plural = TAGS_VERBOSE_NAME_016
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag016.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step016(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic016, related_name='steps016', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag016, related_name="steps016", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author016, related_name='steps016', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_016
        verbose_name_plural = STEP_VERBOSE_NAME_016
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment016(models.Model):
    step = models.ForeignKey('Step016', on_delete=models.CASCADE, related_name='comments016', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_016
        verbose_name_plural = COMMENTS_VERBOSE_NAME_016
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017 017

class Author017(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_017
        verbose_name_plural = AUTHOR_VERBOSE_NAME_017
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic017(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_017
        verbose_name_plural = TOPIC_VERBOSE_NAME_017
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic017(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic017, related_name='subtopics017', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_017
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_017
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag017(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag017"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_017
        verbose_name_plural = TAGS_VERBOSE_NAME_017
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag017.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step017(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic017, related_name='steps017', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag017, related_name="steps017", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author017, related_name='steps017', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_017
        verbose_name_plural = STEP_VERBOSE_NAME_017
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment017(models.Model):
    step = models.ForeignKey('Step017', on_delete=models.CASCADE, related_name='comments017', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_017
        verbose_name_plural = COMMENTS_VERBOSE_NAME_017
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018 018

class Author018(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_018
        verbose_name_plural = AUTHOR_VERBOSE_NAME_018
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic018(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_018
        verbose_name_plural = TOPIC_VERBOSE_NAME_018
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic018(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic018, related_name='subtopics018', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_018
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_018
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag018(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag018"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_018
        verbose_name_plural = TAGS_VERBOSE_NAME_018
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag018.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step018(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic018, related_name='steps018', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag018, related_name="steps018", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author018, related_name='steps018', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_018
        verbose_name_plural = STEP_VERBOSE_NAME_018
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])
    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')
    def clean(self):
        if len(self.slug) > 150:
            raise ValidationError({'slug': "Поле 'slug' слишком длинное. Максимум 150 символов."})
        if len(self.seo_description) > 350:
            raise ValidationError({'seo_description': "Поле 'seo_description' слишком длинное. Максимум 350 символов."})
        if len(self.keyword) > 150:
            raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if self.keyword:
            if len(self.keyword) > 150:
                raise ValidationError({'keyword': "Поле 'keyword' слишком длинное. Максимум 150 символов."})
        if len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if len(self.h1) > 150:
            raise ValidationError({'h1': "Поле 'h1' слишком длинное. Максимум 150 символов."})
        if len(self.image_file_name) > 150:
            raise ValidationError({'image_file_name': "Поле 'image_file_name' слишком длинное. Максимум 150 символов."})
        if len(self.image_alt_and_prompt) > 150:
            raise ValidationError \
                ({'image_alt_and_prompt': "Поле 'image_alt_and_prompt' слишком длинное. Максимум 150 символов."})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.is_published and not self.published_date:
            self.published_date = now()
        if not self.slug:
            clean_title = self.title.strip().replace('\r', '').replace('\n', '')
            self.slug = slugify(clean_title, allow_unicode=True)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)


class Comment018(models.Model):
    step = models.ForeignKey('Step018', on_delete=models.CASCADE, related_name='comments018', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата одобрения")
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_018
        verbose_name_plural = COMMENTS_VERBOSE_NAME_018
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


# 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101

class Author101(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True,
                                       verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_101
        verbose_name_plural = AUTHOR_VERBOSE_NAME_101

    def __str__(self):
        return self.type


class Topic101(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True,
                                       verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = TOPIC_VERBOSE_NAME_101
        verbose_name_plural = TOPIC_VERBOSE_NAME_101

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic101(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True,
                                       verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic101, related_name='subtopics101', on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_101
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_101

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag101(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    class Meta:
        db_table = "tag101"
        verbose_name = TAGS_VERBOSE_NAME_101
        verbose_name_plural = TAGS_VERBOSE_NAME_101
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name.lower(), allow_unicode=True)
            base_slug = self.slug
            counter = 1
            while Tag101.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


import os
import re
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.text import slugify


class Step101(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок title", blank=True, null=True)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    subtitle = models.CharField(max_length=150, verbose_name="Подзаголовок")
    brands = models.CharField(max_length=150, verbose_name="Бренды")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    plus_minus = models.TextField('Плюсы и Минусы', blank=True, default='', max_length=1000)
    expert_opinion = models.TextField(blank=True, verbose_name="Экспертное мнение", max_length=11000)
    expert_recommendation = models.BooleanField(default=False, verbose_name="Рекомендует")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    image_file_name = models.CharField(max_length=150, blank=True, null=True,
                                       verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    tags = models.ManyToManyField(Tag101, related_name="steps101", blank=True, verbose_name="теги")
    subtopic = models.ForeignKey(
        Subtopic101,
        related_name='steps101',
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Подтема",
        blank=True,
        null=True,
        default=None
    )
    author_type = models.ForeignKey(
        Author101,
        related_name='steps101',
        on_delete=models.CASCADE,
        verbose_name="Автор",
        blank=True,
        null=True
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        allow_unicode=True,
        max_length=150,
        verbose_name="Слуг",
        blank=True,
        null=True
    )
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    possible_categories = models.TextField('Возможные категории', blank=True, default='')
    possible_tags = models.TextField('Возможные теги', blank=True, default='')

    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
            models.Index(fields=['subtitle']),
            models.Index(fields=['brands']),
        ]
        verbose_name = STEP_VERBOSE_NAME_101
        verbose_name_plural = STEP_VERBOSE_NAME_101

    def __str__(self):
        return self.h1

    def get_absolute_url(self):
        return reverse('step_detail', args=[self.slug])

    @property
    def formatted_updated_date(self):
        return self.updated_date.strftime('%d.%m.%Y')

    def clean(self):
        if self.title and len(self.title) > 150:
            raise ValidationError({'title': "Поле 'title' слишком длинное. Максимум 150 символов."})
        if self.description and len(self.description) > 11000:
            raise ValidationError({'description': "Поле 'description' слишком длинное. Максимум 11000 символов."})
        if self.expert_opinion and len(self.expert_opinion) > 11000:
            raise ValidationError({'expert_opinion': "Поле 'expert_opinion' слишком длинное. Максимум 11000 символов."})

    def save(self, *args, **kwargs):
        # Полная валидация
        self.full_clean()

        # 1. Авто-установка даты публикации
        if self.is_published:
            # Если даты нет или она равна минимальной "0001-01-01"
            if not self.published_date or str(self.published_date).startswith("0001-01-01"):
                self.published_date = now()
        else:
            # Если запись снята с публикации → дата сбрасывается
            self.published_date = None

        # 2. Генерация slug
        if not self.slug:
            base = self.keyword or self.h1 or self.title
            if base:
                clean_base = base.strip().replace('\r', '').replace('\n', '')
                clean_base = re.sub(r'\s+', '-', clean_base)
                clean_base = re.sub(r'[^\w\-а-яА-ЯёЁ]', '', clean_base)
                self.slug = slugify(clean_base, allow_unicode=True)

        # 3. Имя файла картинки
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]

        # 4. Подтягивание подкатегории "Отзывы"
        if not self.subtopic_id:
            default_subtopic = Subtopic101.objects.filter(title__iexact="Отзывы").first()
            if default_subtopic:
                self.subtopic = default_subtopic

        # 5. Сохранение
        super().save(*args, **kwargs)


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now


class Comment101(models.Model):
    step = models.ForeignKey(
        'Step101',
        on_delete=models.CASCADE,
        related_name='comments101',
        db_index=True,
        verbose_name="Шаг"
    )

    username = models.CharField(
        max_length=100,
        default="Аноним",
        verbose_name="Имя пользователя"
    )

    text = models.TextField(
        verbose_name="Текст комментария"
    )

    is_positive = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name="Позитивный комментарий"
    )

    rating = models.PositiveIntegerField(
        default=0,
        db_index=True,
        verbose_name="Лайки"
    )

    created_date = models.DateTimeField(
        default=now,
        verbose_name="Дата создания"
    )

    is_published = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name="Опубликован"
    )

    published_date = models.DateTimeField(
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Дата одобрения"
    )

    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = now()
        elif not self.is_published:
            self.published_date = None

        super().save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=['step', 'is_published', 'published_date']),
            models.Index(fields=['rating']),
        ]
        verbose_name = COMMENTS_VERBOSE_NAME_101
        verbose_name_plural = COMMENTS_VERBOSE_NAME_101

    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"

    @property
    def formatted_created_date(self):
        return self.created_date.strftime('%d.%m.%Y')

    @property
    def formatted_published_date(self):
        if not self.published_date:
            return None
        return self.published_date.strftime('%d.%m.%Y')



# ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001

class ZAuthor001(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to='authors/', blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "ZAuthor001"
        verbose_name_plural = "ZAuthor001"

    def __str__(self):
        return self.type

def custom_slugify2(value):
    value = re.sub(r'[^\w\s\-]', '', value)
    value = re.sub(r'\s+', '-', value)
    value = value.lower()
    return value


class ZRubrics001(models.Model):
    name_original = models.CharField('Рубрика', max_length=1000, null=True, blank=True, default='')
    visible = models.BooleanField('Отображать', default=False)
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=1000)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify2(self.name_original)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name_original)


class ZCompany001(models.Model):
    rubrics = models.ManyToManyField('ZRubrics001', blank=True)
    org_name1 = models.CharField('Название 1', max_length=1000, null=True, blank=True, default='')
    org_name2 = models.CharField('Название 2', max_length=1000, blank=True, default='')
    org_name3 = models.CharField('Название 3', max_length=1000, blank=True, default='')
    mainnew = models.TextField('Адрес', null=True, blank=True, default='')
    address_comment = models.CharField('Комментарий', max_length=1000, null=True, blank=True, default='')
    contact_groups_contacts1_text1 = models.CharField('Контакт', max_length=1000, blank=True, default='')
    contact_groups_contacts1_text2 = models.CharField('Контакт', max_length=1000, blank=True, default='')
    contact_groups_contacts1_text3 = models.CharField('Контакт', max_length=1000, blank=True, default='')
    contact_groups_contacts2_text1 = models.CharField('Контакт', max_length=1000, blank=True, default='')
    contact_groups_contacts2_text2 = models.CharField('Контакт', max_length=1000, blank=True, default='')
    contact_groups_contacts2_text3 = models.CharField('Контакт', max_length=1000, blank=True, default='')
    ads_article = models.CharField('Инфо', max_length=3000, blank=True, default='')
    article_warning = models.CharField('Доп инфо', max_length=1000, blank=True, default='')
    description = models.TextField('Описание', blank=True, default='')
    plus_minus = models.TextField('Плюсы и Минусы', blank=True, default='')
    expert_opinion = models.TextField('Экспертное мнение', blank=True, default='', max_length=11000)
    expert_recommendation = models.BooleanField('Рекомендует', default=False)

    # 🔥 новое поле — автор экспертного мнения
    author_expert = models.ForeignKey(
        'ZAuthor001', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Автор экспертного мнения"
    )

    visible = models.BooleanField('Отображать', default=True, null=True)
    pro = models.BooleanField('PRO', null=True, default=False)
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=1000)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    possible_categories = models.TextField('Возможные категории', blank=True, default='')
    possible_tags = models.TextField('Возможные теги', blank=True, default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify2(self.org_name1)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.org_name1)


class ZCompanyRubrics001(models.Model):
    company = models.ForeignKey(ZCompany001, on_delete=models.CASCADE)
    rubric = models.ForeignKey(ZRubrics001, on_delete=models.CASCADE)


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class ZComment001(models.Model):
    company = models.ForeignKey(
        'ZCompany001',
        on_delete=models.CASCADE,
        related_name='zcomments001'
    )

    name = models.CharField(
        max_length=300,
        default='Anonymous'
    )

    content = models.TextField()

    is_positive = models.BooleanField(
        default=True
    )

    published = models.BooleanField(
        'Is published',
        default=False
    )

    rating = models.PositiveIntegerField(
        default=0,
        db_index=True,
        verbose_name="Лайки"
    )

    created_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()

        if self.published:
            self.created_at = timezone.now()

        super().save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=['company', 'published', 'created_at']),
            models.Index(fields=['rating']),
        ]

    def __str__(self):
        return f"{self.name} ({self.created_at:%d.%m.%Y})"


class ZFileTracker001(models.Model):
    filename = models.CharField(max_length=255)