from .models import custom_slugify
from .models import Tag001, Author001, Topic001, Subtopic001, Step001, Comment001
from .models import Tag002, Author002, Topic002, Subtopic002, Step002, Comment002
from .models import Tag003, Author003, Topic003, Subtopic003, Step003, Comment003
from .models import Tag004, Author004, Topic004, Subtopic004, Step004, Comment004
from .models import Tag005, Author005, Topic005, Subtopic005, Step005, Comment005
from .models import Tag006, Author006, Topic006, Subtopic006, Step006, Comment006
from .models import Tag007, Author007, Topic007, Subtopic007, Step007, Comment007
from .models import Tag008, Author008, Topic008, Subtopic008, Step008, Comment008
from .models import Tag009, Author009, Topic009, Subtopic009, Step009, Comment009
from .models import Tag010, Author010, Topic010, Subtopic010, Step010, Comment010
from .models import Tag011, Author011, Topic011, Subtopic011, Step011, Comment011
from .models import Tag012, Author012, Topic012, Subtopic012, Step012, Comment012
from .models import Tag013, Author013, Topic013, Subtopic013, Step013, Comment013
from .models import Tag014, Author014, Topic014, Subtopic014, Step014, Comment014
from .models import Tag015, Author015, Topic015, Subtopic015, Step015, Comment015
from .models import Tag016, Author016, Topic016, Subtopic016, Step016, Comment016
from .models import Tag017, Author017, Topic017, Subtopic017, Step017, Comment017
from .models import Tag018, Author018, Topic018, Subtopic018, Step018, Comment018
from .models import Tag101, Author101, Topic101, Subtopic101, Step101, Comment101
from django.core.exceptions import ValidationError
from django.utils.timezone import now
import re
import logging
from django.utils.text import slugify
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from urllib.parse import unquote
from django.urls import reverse
from django.shortcuts import render
from .abc import SUFFIX
from django.apps import apps
from django.core.paginator import Paginator
from .forms import Step101Form
from django.db.models import Q, Count
from django.contrib import messages
import os
import random
import logging
import datetime
import json
from urllib.parse import unquote
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse


def create_unique_slug(base_slug, model):
    slug = slugify(base_slug, allow_unicode=True)
    base_slug = slug
    counter = 1
    while model.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug


def extract_between(text, start, end):
    if start:
        text = text.split(start, 1)[-1]
    if end:
        text = text.split(end, 1)[0]
    return text.strip()



def test2(request):

    steps_list = Step101.objects.all().order_by('published_date')

    paginator = Paginator(steps_list, 30)

    page_number = request.GET.get('page')
    steps = paginator.get_page(page_number)

    return render(request, 'data/test2.html', {'steps': steps})





import random

def maybe(prob, func):
    if random.random() * 100 < prob:
        return func()
    return None

def weighted_choice(choices, num_reviews=None):
    filtered_choices = choices
    if num_reviews is not None and num_reviews == 1:
        filtered_choices = [c for c in choices if len(c) < 3 or not c[2]]
    if not filtered_choices:
        return None
    values = [c[0] for c in filtered_choices]
    weights = [c[1] for c in filtered_choices]
    return random.choices(values, weights=weights)[0]


def get_brands_list(step):
    """Преобразует строку брендов в список и возвращает случайный бренд"""
    if not step.brands:
        return None
    brands = [b.strip() for b in step.brands.split(",") if b.strip()]
    if not brands:
        return None
    return random.choice(brands)


def generate_reviews_context(step=None, num_reviews=10):
    """Генерация контекстов отзывов с реалистичными шансами появления блоков."""
    ranges = [
        (30, 100),
        (30, 200),
        (30, 300),
        (100, 400),
        (100, 500),
        (100, 600),
        (100, 700),
        (30, 800),
        (30, 1000),
        (30, 2000)
    ]
    random.shuffle(ranges)
    reviews_context = []
    brand = get_brands_list(step)
    for i in range(num_reviews):
        brand = get_brands_list(step)
        min_len, max_len = ranges[i % len(ranges)]
        company_name_variants = [
            ("не указывать", 75),
            (f"указать в отзыве: {brand} (изменить окончание под контекст, если это уместно, если нет - не менять окончание и указать в точности)"
             if brand is not None
             else "указать в отзыве (изменить окончание под контекст, если это уместно, если нет - не менять окончание и указать в точности)",
             21),
            (f"указать в отзыве: {brand} (не менять окончание под контекст и указать в точности)"
             if brand is not None
             else "указать в отзыве (не менять окончание под контекст и указать в точности)", 1),
            (f"указать в отзыве: {brand} (если в бренде цифры - расшифровывать/перевести в слова)"
             if brand is not None
             else "указать в отзыве (если в бренде цифры - расшифровывать/перевести в слова)", 1),
            (f"указать в отзыве: {brand} (если бренд из нескольких слов - написать без пробелов, а если из 1 - то пробелы вокруг бренда указываем)"
             if brand is not None
             else "указать в отзыве (если бренд из нескольких слов - написать без пробелов, а если из 1 - то пробелы вокруг бренда указываем)", 0.5),
            (f"указать в отзыве: {brand} (если бренд на рус или англ - сделать транслит в другую сторону)"
             if brand is not None
             else "указать в отзыве (если бренд на рус или англ - сделать транслит в другую сторону)", 1),
            (f"указать в отзыве: {brand} (если бренд на русском - сделать перевод на англ, если на англ - сделать перевод на русский)"
             if brand is not None
             else "указать в отзыве (если бренд на русском - сделать перевод на англ, если на англ - сделать перевод на русский)", 0.5),
        ]
        realism_variants = [
            ("начинает отзыв без вступления — сразу с сути, и слова с ё пишет через е", 20),
            ("делает отзыв коротким без 'но' и переходов, и слова с ё пишет через е", 15),
            ("добавляет опечатки или ошибки в словах, и слова с ё пишет через е", 15),
            ("смешивает предложения разной длины для естественности, и слова с ё пишет через е", 10),
            ("пишет несколько пунктов про ошибки или достоинства, и слова с ё пишет через е", 5),
            ("разделяет отзыв на 2 или несколько абзацев (ставит энтеры), если отзыв может делиться на абзацы, а если короткий - не разделяет", 5),
            ("в основном пишет одним предложением", 5),
            ("в отзыве чувствуется смена настроения — от нейтрального к эмоциональному", 5),
            ("иногда пропускает запятые для реалистичности, и слова с ё пишет через е", 12),
            ("в середине отзыва делает длинное предложение, потом короткое", 1),
            ("в конце отзыва не ставит точку, только между другими предложениями", 1.5),
            ("не пишет с большой буквы первые слова в предложениях", 0.5),
            ("повторяет слова или выражения для усиления эмоции", 0.5),
            ("вставляет междометия вроде 'эээ', 'мм', 'ну', 'вот', 'как бы'", 0.5),
            ("иногда использует смайлики или эмодзи", 0.5),
            ("вставляет многоточия для паузы или эмоции", 0.5),
            ("ставит несколько восклицательных знаков подряд", 0.5),
            ("использует капслок в одном-двух словах для эмоций", 0.5),
            ("добавляет кавычки для выделения слов или сарказма", 0.5),
            ("использует слова-паразиты ('типа', 'в общем', 'короче' и другие)", 0.5),
            ("использует неформальные сокращения ('щас', 'че', 'ток', 'вообщем')", 0.5),
            ("начинает отзыв с 'в целом', 'ну', 'честно говоря', 'если коротко' и т.п.", 0.25),
            ("иногда пишет всё строчными буквами", 0.25),
        ]
        data = {
            "words": random.randint(min_len, max_len),
            "style": weighted_choice([
                ("формальный", 35),
                ("неформальный", 30),
                ("повествовательный", 20),
                ("разговорный", 10),
                ("дружелюбный", 5),
            ]),
            "type": weighted_choice([
                ("позитивный", 30),
                ("умеренно позитивный", 20),
                ("нейтральный", 20),
                ("умеренно негативный", 15),
                ("негативный", 15),
            ]),
            "tone": weighted_choice([
                ("спокойный", 35),
                ("эмоциональный", 20),
                ("уверенный", 15),
                ("разговорный", 10),
                ("вежливый", 10),
                ("ироничный", 10),
            ]),
            "speech": weighted_choice([
                ("разговорная речь с местными словами", 25),
                ("упрощённые фразы, как у обычного клиента", 25),
                ("сленг и разговорные выражения", 17),
                ("грамотная речь без излишеств", 15),
                ("нейтральный стиль общения", 15),
                ("с акцентом какой-то страны из СНГ", 3),
            ]),
            "oborots": maybe(15, lambda: weighted_choice([
                ("часто использует эмоции", 10),
                ("редко использует вводные слова", 20),
                ("иногда делает акценты", 15),
                ("использует повторы для усиления", 15),
                ("упрощает предложения для естественности", 30),
                ("использует метафоры или сравнения", 5),
                ("добавляет риторические вопросы", 5),
            ])),
            "some": maybe(25, lambda: weighted_choice([
                ("эмоций", 5),
                ("деталей", 40),
                ("примеров", 20),
                ("личных наблюдений", 10),
                ("конкретных ситуаций", 15),
                ("сравнений с другими компаниями", 5),
                ("ссылок на личный опыт", 5),
            ])),
            "context": maybe(15, lambda: weighted_choice([
                ("комментирует качество услуг", 20),
                ("отмечает скорость ответа", 10),
                ("спрашивает про цены", 17),
                ("пишет про атмосферу компании", 10),
                ("делится впечатлением от сервиса", 10),
                ("упоминает удобство сайта или приложения", 10),
                ("говорит о гарантии", 10),
                ("говорит о возврате", 10),
                ("говорит о доставке", 3),
            ])),
            "add": maybe(15, lambda: weighted_choice([
                ("продолжает обсуждение темы статьи", 20),
                ("добавляет что-то новое", 20),
                ("задаёт уточняющий вопрос", 10),
                ("задаёт уточняющий вопрос одному из комментаторов (предыдущих)", 5, True),
                ("выражает мнение без категоричности", 10),
                ("комментирует работу персонала", 10),
                ("даёт совет другим пользователям", 5, True),
                ("даёт совет другому пользователю упоминая его ник/имя", 5, True),
                ("пишет, что подумает обратиться снова", 5),
                ("упоминает альтернативные варианты", 5),
                ("упоминает время года или событие", 5),
            ], num_reviews)),
            "interaction": maybe(15, lambda: weighted_choice([
                ("спрашивает совета у других пользователей", 15, True),
                ("комментирует чужой отзыв", 35, True),
                ("благодарит другого комментатора за полезную информацию", 15, True),
                ("отвечает на вопрос другого пользователя, если вопрос был в других отзывах выше (предыдущих)", 15, True),
                ("вовлекает других в обсуждение", 10, True),
                ("соглашается с предыдущим отзывом", 5, True),
                ("спорит с чужим мнением вежливо", 5, True),
            ], num_reviews)),
            "company_name_instruction": weighted_choice(company_name_variants),
            "realism": maybe(70, lambda: weighted_choice(realism_variants))
        }
        # Удаляем пустые значения
        data = {k: v for k, v in data.items() if v}
        reviews_context.append(data)
    # 🔸 Переносим «интерактивные» отзывы в конец
    interactive = [r for r in reviews_context if "interaction" in r]
    non_interactive = [r for r in reviews_context if "interaction" not in r]
    return non_interactive + interactive


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.utils.timezone import now
import random


def step_detail2(request, slug):
    # Убираем фильтр is_published=True — теперь страница найдётся, даже если не опубликована
    step = get_object_or_404(Step101, slug=slug)

    message = ''  # для уведомления о сохранении
    active_tab = 'Expert'  # по умолчанию активная вкладка

    # Можно при желании визуально отметить, что страница не опубликована
    show_unpublished_notice = not step.is_published

    comments = step.comments101.filter(is_published=True).order_by('-created_date')

    num = request.GET.get('num', 'random')
    if num == 'random':
        num_reviews = random.randint(1, 10)
    else:
        num_reviews = min(max(int(num), 1), 10)

    reviews_context = None
    if 'generate_reviews_context' in globals():
        reviews_context = generate_reviews_context(step=step, num_reviews=num_reviews)

    if request.method == 'POST':
        fake_field = request.POST.get('fake_field', '').strip()
        if fake_field:
            return HttpResponseForbidden('Вы не можете отправлять комментарии.')

        # Определяем, какая форма была отправлена
        if 'expert_opinion' in request.POST:
            expert_opinion = request.POST.get('expert_opinion', '').strip()
            plus_minus = request.POST.get('plus_minus', '').strip()
            expert_recommendation = request.POST.get('expert_recommendation') == 'on'

            possible_categories = request.POST.get('possible_categories', '').strip()
            possible_tags = request.POST.get('possible_tags', '').strip()
            description = request.POST.get('description', '').strip()

            step.expert_opinion = expert_opinion
            step.plus_minus = plus_minus
            step.expert_recommendation = expert_recommendation

            step.possible_categories = possible_categories
            step.possible_tags = possible_tags
            step.description = description

            # получаем имя/строку автора из формы
            author_expert_name = request.POST.get('author_expert', '').strip()

            if author_expert_name:
                # сначала пытаемся найти по title (чувствительность игнорируем) или по type
                author = Author101.objects.filter(title__iexact=author_expert_name).first()
                if not author:
                    author = Author101.objects.filter(type__iexact=author_expert_name).first()

                # если не нашли — создаём минимальную запись (type + title + h1)
                if not author:
                    author = Author101.objects.create(
                        type=author_expert_name,
                        title=author_expert_name,
                        h1=author_expert_name,
                        is_published=False
                    )

                step.author_type = author

            step.save()
            message = 'UPDATED!'
            active_tab = 'Expert'




        elif 'name' in request.POST and 'content' in request.POST:
            # --- Форма комментариев ---
            username = request.POST.get('name', '').strip()
            text = request.POST.get('content', '').strip()
            feedback_type = request.POST.get('feedback_type', '').strip()
            if username and text and feedback_type in ['positive', 'negative']:
                is_positive = (feedback_type == 'positive')
                Comment101.objects.create(
                    step=step,
                    username=username,
                    text=text,
                    is_positive=is_positive,
                    created_date=now(),
                    is_published=False
                )
                message = 'ADDED!'  # сообщение для шаблона
                active_tab = 'AddReview'

                comments = step.comments101.filter(is_published=True).order_by('-created_date')

    return render(request, 'data/step_detail2.html', {
        'step': step,
        'comments': comments,
        'reviews_context': reviews_context,
        'num_reviews': num_reviews,
        'selected_num': num,
        'show_unpublished_notice': show_unpublished_notice,
        'message': message,
        'active_tab': active_tab,  # передаем активную вкладку в шаблон
    })





def add_step101(request):
    if request.method == 'POST':
        form = Step101Form(request.POST)
        if form.is_valid():
            step = form.save(commit=False)

            # подтема "Отзывы"
            step.subtopic = Subtopic101.objects.filter(title__icontains="Отзывы").first()

            # автор по умолчанию "Клиент"
            step.author_type = Author101.objects.filter(type__icontains="Клиент").first()

            # slug = keyword (через дефисы и lowercase)
            if step.keyword:
                step.slug = slugify(step.keyword, allow_unicode=True)

            # дискрипшн -> seo_description
            step.seo_description = form.cleaned_data.get('description', '')

            # сразу опубликовано
            step.is_published = True
            step.published_date = now()

            step.save()
            return redirect(step.get_absolute_url())
    else:
        form = Step101Form()

    return render(request, 'data/add_step101.html', {'form': form})


def create_step_for_reviews_only(request):
    context = {}
    if request.method == 'POST':
        raw_text = request.POST.get('text', '')
        clean_text = raw_text.replace('**Ответ от автора сайта:**', '').strip()

        try:
            description = re.sub(r'(-{3,}|—{5,})', '', extract_between(clean_text, '**Ответ от автора сайта:**',
                                                                       '**Заголовок title:**')).strip()
            title = extract_between(clean_text, '**Заголовок title:**', '**Заголовок h1:**').strip()
            h1 = extract_between(clean_text, '**Заголовок h1:**', '**Ключевая фраза:**').strip()
            subtitle = extract_between(clean_text, '**Подзаголовок:**', '**Бренды:**').strip()
            brands = extract_between(clean_text, '**Бренды:**', '**Заголовок title:**').strip()

            keyword = extract_between(clean_text, '**Ключевая фраза:**', '**Ключевые фразы keywords:**').strip()
            keywords = extract_between(clean_text, '**Ключевые фразы keywords:**',
                                        '**Название картинки для файла:**').strip()
            image_file_name = extract_between(clean_text, '**Название картинки для файла:**',
                                              '**Описание картинки:**').strip()
            image_alt_and_prompt = extract_between(clean_text, '**Описание картинки:**', '**Категория:**').strip()
            subtopic_title = extract_between(clean_text, '**Категория:**', '**Теги:**').strip()
            tags = extract_between(clean_text, '**Теги:**', '**Тип автора:**').strip()
            author_type = extract_between(clean_text, '**Тип автора:**', '**Дискрипшн:**').strip()
            seo_description = extract_between(clean_text, '**Дискрипшн:**', '**Сайт:**').strip()
            site = extract_between(clean_text, '**Сайт:**', '**Мини-фраза:**').strip()

            base_slug = custom_slugify(
                extract_between(clean_text, '**Мини-фраза:**', '**Имя пользователя 1:**').strip()
            )

            if site == "отзывы.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author101, Tag101, Topic101, Subtopic101, Step101, Comment101
                )
            elif site == "банк.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author002, Tag002, Topic002, Subtopic002, Step002, Comment002
                )
            elif site == "здоровье.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author003, Tag003, Topic003, Subtopic003, Step003, Comment003
                )
            elif site == "авто-мото.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author004, Tag004, Topic004, Subtopic004, Step004, Comment004
                )
            elif site == "хайтек.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author005, Tag005, Topic005, Subtopic005, Step005, Comment005
                )
            elif site == "юрист.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author006, Tag006, Topic006, Subtopic006, Step006, Comment006
                )
            elif site == "бухгалтер.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author007, Tag007, Topic007, Subtopic007, Step007, Comment007
                )
            elif site == "психолог.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author008, Tag008, Topic008, Subtopic008, Step008, Comment008
                )
            elif site == "бытовая-техника.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author009, Tag009, Topic009, Subtopic009, Step009, Comment009
                )
            elif site == "работа.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author010, Tag010, Topic010, Subtopic010, Step010, Comment010
                )
            elif site == "огород.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author011, Tag011, Topic011, Subtopic011, Step011, Comment011
                )
            elif site == "сво.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author012, Tag012, Topic012, Subtopic012, Step012, Comment012
                )
            elif site == "животные.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author013, Tag013, Topic013, Subtopic013, Step013, Comment013
                )
            elif site == "курсы.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author014, Tag014, Topic014, Subtopic014, Step014, Comment014
                )
            elif site == "еда.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author015, Tag015, Topic015, Subtopic015, Step015, Comment015
                )
            elif site == "мистика.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author016, Tag016, Topic016, Subtopic016, Step016, Comment016
                )
            elif site == "недвижимость.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author017, Tag017, Topic017, Subtopic017, Step017, Comment017
                )
            elif site == "стройка-и-ремонт.рф":
                author_model, tag_model, topic_model, subtopic_model, step_model, comment_model = (
                    Author018, Tag018, Topic018, Subtopic018, Step018, Comment018
                )
            else:
                raise Exception(f"Unsupported site: {site}")

            topic_instance, _ = topic_model.objects.get_or_create(title="Отзывы")

            subtopic_instance, _ = subtopic_model.objects.get_or_create(title=subtopic_title)
            subtopic_instance.topic = topic_instance
            subtopic_instance.save()

            author_type_instance, _ = author_model.objects.get_or_create(type=author_type)

            tags_list = [tag.strip().lower() for tag in tags.split(',') if tag.strip()]
            tag_instances = []

            with transaction.atomic():
                for tag in tags_list:
                    tag_slug = create_unique_slug(tag, tag_model)

                    tag_instance, created = tag_model.objects.get_or_create(
                        name=tag,
                        defaults={'slug': tag_slug}
                    )

                    if not isinstance(tag_instance, tag_model):
                        raise Exception(
                            f"Tag instance mismatch: Expected {tag_model.__name__}, got {type(tag_instance).__name__}"
                        )

                    tag_instances.append(tag_instance)

            slug = create_unique_slug(base_slug, step_model)
            step = step_model(
                description=description,
                keyword=keyword,
                keywords=keywords,
                title=title,
                h1=h1,
                subtitle=subtitle,
                brands=brands,
                image_file_name=image_file_name,
                image_alt_and_prompt=image_alt_and_prompt,
                slug=slug,
                author_type=author_type_instance,
                seo_description=seo_description,
                subtopic=subtopic_instance,
                published_date=now(),
                updated_date=now(),
            )
            step.save()
            step.tags.add(*tag_instances)

            for i in range(1, 11):
                username_key = f'**Имя пользователя {i}:**'
                comment_key = f'**Отзыв пользователя {i}:**'
                username = extract_between(clean_text, username_key, comment_key).strip()
                comment_text = extract_between(clean_text, comment_key, f'**Имя пользователя {i + 1}:**').strip()
                if username and comment_text:
                    comment_model.objects.create(
                        step=step,
                        username=username,
                        text=comment_text,
                    )

            context['step'] = step

        except ValidationError as e:
            context['errors'] = e.message_dict
        except Exception as e:
            context['errors'] = {'general': [str(e)]}
            logging.error(f"Error in create_step: {str(e)}")

    return render(request, 'data/for_reviews_only.html', context)


def index(request):
    steps_list = Step101.objects.filter(is_published=True).order_by('-published_date')
    paginator = Paginator(steps_list, 30)  # По 30 шагов на страницу

    page_number = request.GET.get('page')
    steps = paginator.get_page(page_number)

    return render(request, 'data/index.html', {'steps': steps})


def subtopic_list(request, slug):
    model_name = f"Subtopic{SUFFIX}"
    steps_field = f"steps{SUFFIX}"
    Subtopic = apps.get_model('data', model_name)
    subtopic = get_object_or_404(Subtopic, slug=unquote(slug))
    steps = getattr(subtopic, steps_field).filter(is_published=True).order_by('-published_date')
    return render(request, f'data/subtopic_list.html', {'subtopic': subtopic, 'steps': steps})


from django.db.models import Avg


def step_detail(request, slug):
    step_model_name = f"Step{SUFFIX}"
    comment_model_name = f"Comment{SUFFIX}"
    Step = apps.get_model('data', step_model_name)
    Comment = apps.get_model('data', comment_model_name)

    # Получение текущего шага
    step = get_object_or_404(Step, slug=unquote(slug))

    # Получение связанных объектов
    subtopic = step.subtopic
    topic = subtopic.topic
    steps_field = f"steps{SUFFIX}"
    steps = getattr(subtopic, steps_field).all()
    comments_field = f"comments{SUFFIX}"

    # Добавляем выборку is_positive и вычисляем средний рейтинг
    comments = getattr(step, comments_field).filter(is_published=True).order_by('-published_date')

    # Вычисляем средний рейтинг во view
    avg_rating = comments.aggregate(avg_rating=Avg('rating'))['avg_rating']
    if avg_rating:
        avg_rating = round(avg_rating, 1)
    else:
        avg_rating = "0.0"

    if request.method == 'POST':
        honey_pot_value = request.POST.get('honey_pot', '').strip()
        if honey_pot_value:
            return redirect('step_detail', slug=slug)

        text = request.POST.get('content', '').strip()
        username = (
            request.POST.get('user_name', '').strip()
            if not request.user.is_authenticated
            else request.user.username
        )
        if text:
            Comment.objects.create(
                step=step,
                text=text,
                username=username or "Аноним"
            )
            return redirect('step_detail', slug=slug)

    # Рендеринг страницы
    return render(
        request,
        f'data/step_detail.html',
        {
            'topic': topic,
            'subtopic': subtopic,
            'step': step,
            'steps': steps,
            'comments': comments,
            'avg_rating': avg_rating,  # Передаем вычисленный рейтинг в контекст
        }
    )


def add_comment(request, step_slug):
    comment_model_name = f"Comment{SUFFIX}"
    Comment = apps.get_model('data', comment_model_name)

    step_model_name = f"Step{SUFFIX}"
    Step = apps.get_model('data', step_model_name)

    step = get_object_or_404(Step, slug=step_slug)
    if request.method == "POST":
        content = request.POST.get("content", "").strip()
        user_name = request.POST.get("user_name",
                                     "").strip() if not request.user.is_authenticated else request.user.username
        if not content or (not user_name and not request.user.is_authenticated):
            return HttpResponseRedirect(reverse('step_detail', args=[step.slug]))
        Comment.objects.create(
            step=step,
            content=content,
            user_name=user_name if not request.user.is_authenticated else None,
            user=request.user if request.user.is_authenticated else None
        )
        return HttpResponseRedirect(reverse('step_detail', args=[step.slug]))


from django.shortcuts import render, redirect
from .forms import BulkStepForm
from .models import Step101
from django.utils.text import slugify

def bulk_create_steps(request):
    message = None

    if request.method == "POST":
        form = BulkStepForm(request.POST)
        if form.is_valid():
            raw = form.cleaned_data['raw_text']
            lines = raw.split("\n")
            created = 0

            for line in lines:
                if "|||" not in line:
                    continue

                parts = [p.strip() for p in line.split("|||") if p.strip()]

                if len(parts) < 5:
                    continue  # Not enough fields

                h1 = parts[0]
                subtitle = parts[1]
                brands = parts[2]
                keyword = parts[3]
                slug = parts[4]

                Step101.objects.create(
                    h1=h1,
                    subtitle=subtitle,
                    brands=brands,
                    keyword=keyword,
                    slug=slug,
                    title=h1,                 # можно адаптировать
                    description="",           # или автогенерация
                    expert_opinion="",
                    image_file_name="",
                    image_alt_and_prompt="",
                    seo_description=""
                )
                created += 1

            message = f"Создано объектов: {created}"
            return render(request, "data/bulk_steps.html", {"form": form, "message": message})

    else:
        form = BulkStepForm()

    return render(request, "data/bulk_steps.html", {"form": form})
