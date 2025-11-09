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


class Author002(models.Model):
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
        verbose_name = AUTHOR_VERBOSE_NAME_002
        verbose_name_plural = AUTHOR_VERBOSE_NAME_002
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])


class Topic002(models.Model):
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
        verbose_name = TOPIC_VERBOSE_NAME_002
        verbose_name_plural = TOPIC_VERBOSE_NAME_002
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Subtopic002(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    h1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Заголовок h1")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    topic = models.ForeignKey(Topic002, related_name='subtopics002', on_delete=models.CASCADE, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        if self.image and not self.image_file_name:
            self.image_file_name = os.path.splitext(os.path.basename(self.image.name))[0]
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = SUBTOPIC_VERBOSE_NAME_002
        verbose_name_plural = SUBTOPIC_VERBOSE_NAME_002
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('subtopic_list', args=[self.slug])


class Tag002(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")
    class Meta:
        db_table = "tag002"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_002
        verbose_name_plural = TAGS_VERBOSE_NAME_002
        ordering = ['name']
    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)
            base_slug = self.slug
            counter = 1
            while Tag002.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name


class Step002(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic002, related_name='steps002', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag002, related_name="steps002", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author002, related_name='steps002', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")
    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_002
        verbose_name_plural = STEP_VERBOSE_NAME_002
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


class Comment002(models.Model):
    step = models.ForeignKey('Step002', on_delete=models.CASCADE, related_name='comments002', db_index=True, verbose_name="Шаг")
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
        verbose_name = COMMENTS_VERBOSE_NAME_002
        verbose_name_plural = COMMENTS_VERBOSE_NAME_002
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')


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
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME_101
        verbose_name_plural = AUTHOR_VERBOSE_NAME_101
    def __str__(self):
        return self.type
    # def get_absolute_url(self):
    #     return reverse('author_detail', args=[self.id])

class Topic101(models.Model):
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
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
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
        db_table = "tag101"  # Явное указание таблицы
        verbose_name = TAGS_VERBOSE_NAME_101
        verbose_name_plural = TAGS_VERBOSE_NAME_101
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага только если он не задан
            self.slug = slugify(self.name.lower(), allow_unicode=True)

            # Проверка уникальности слага
            base_slug = self.slug
            counter = 1
            while Tag101.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step101(models.Model):
    description = models.TextField(blank=True, verbose_name="Описание", max_length=11000)
    title = models.CharField(max_length=150, verbose_name="Заголовок title")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок h1")
    subtitle = models.CharField(max_length=150, verbose_name="Подзаголовок")
    brands = models.CharField(max_length=150, verbose_name="Бренды")
    keyword = models.CharField(max_length=150, blank=True, null=True, unique=True, verbose_name="Ключевая фраза")
    keywords = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ключевые фразы")
    image = models.ImageField(upload_to=get_upload_to, blank=True, null=True, verbose_name="Картинка")
    image_file_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Название картинки для файла")
    image_alt_and_prompt = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание картинки")
    subtopic = models.ForeignKey(Subtopic101, related_name='steps101', on_delete=models.CASCADE, db_index=True, verbose_name="Подтема")
    tags = models.ManyToManyField(Tag101, related_name="steps101", blank=True, verbose_name="теги")
    author_type = models.ForeignKey(Author101, related_name='steps101', on_delete=models.CASCADE, verbose_name="Автор")
    seo_description = models.CharField(max_length=350, blank=True, null=True, verbose_name="Дискрипшн")
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, max_length=150, verbose_name="Слуг")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликовано")
    published_date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")


    class Meta:
        indexes = [
            models.Index(fields=['is_published', 'published_date']),
        ]
        verbose_name = STEP_VERBOSE_NAME_101
        verbose_name_plural = STEP_VERBOSE_NAME_101
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


class Comment101(models.Model):
    step = models.ForeignKey('Step101', on_delete=models.CASCADE, related_name='comments101', db_index=True, verbose_name="Шаг")
    username = models.CharField(max_length=100, default="Аноним", verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Текст комментария")
    is_positive = models.BooleanField(default=False, db_index=True, verbose_name="Позитивный комментарий")
    created_date = models.DateTimeField(default=now, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Опубликован")
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
        verbose_name = COMMENTS_VERBOSE_NAME_101
        verbose_name_plural = COMMENTS_VERBOSE_NAME_101
    def __str__(self):
        return f"Комментарий от {self.username} ({self.created_date:%d.%m.%Y})"
    @property
    def formatted_created_date(self):
        """Возвращает дату создания в формате 'дд.мм.гггг'."""
        return self.created_date.strftime('%d.%m.%Y')



# ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001 ENGIL001




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
    visible = models.BooleanField('Отображать', default=True, null=True)
    pro = models.BooleanField('PRO', null=True, default=False)
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=1000)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify2(self.org_name1)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.org_name1)

    # 👇 Новые удобные методы:
    def comments_published(self):
        """Вернуть только опубликованные комментарии"""
        return self.zcomments001.filter(published=True)

    def comments_count(self):
        """Сколько комментариев всего"""
        return self.zcomments001.count()

    def positive_count(self):
        """Сколько положительных"""
        return self.zcomments001.filter(is_positive=True).count()

    def negative_count(self):
        """Сколько отрицательных"""
        return self.zcomments001.filter(is_positive=False).count()

class ZCompanyRubrics001(models.Model):
    company = models.ForeignKey(ZCompany001, on_delete=models.CASCADE)
    rubric = models.ForeignKey(ZRubrics001, on_delete=models.CASCADE)

from django.utils import timezone

class ZComment001(models.Model):
    company = models.ForeignKey('ZCompany001', on_delete=models.CASCADE, related_name='zcomments001')
    name = models.CharField(max_length=300, default='Anonymous')
    content = models.TextField()
    is_positive = models.BooleanField(default=True)
    published = models.BooleanField('Is published', default=False)
    created_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # ✅ если только что опубликован — обновляем дату
        if self.published:
            self.created_at = timezone.now()
        super().save(*args, **kwargs)


class ZFileTracker001(models.Model):
    filename = models.CharField(max_length=255)