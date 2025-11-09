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

    # Добавляем выборку is_positive
    comments = getattr(step, comments_field).filter(is_published=True).order_by('-published_date')

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
            'comments': comments,  # Теперь comments содержит is_positive
        }
    )


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