from django.urls import path, re_path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import (SubtopicSitemap, StepSitemap)
from .views import test2, add_step101, create_step_for_reviews_only, index, add_comment, subtopic_list, step_detail, step_detail2, bulk_create_steps

sitemaps = {
    'subtopics': SubtopicSitemap,
    'steps': StepSitemap,
}

urlpatterns = [
    path("bulk/", bulk_create_steps, name="bulk_create_steps"),
    path('test2/', test2, name='test2'),
    path('add/', add_step101, name='add_step101'),
    path('for_reviews_only/', create_step_for_reviews_only, name='create_step_for_reviews_only'),

    # ГЛАВНАЯ + ПАГИНАЦИЯ
    path('', index, name='index'),
    path('<int:page>/', index, name='index_page'),

    path('add-comment/<slug:step_slug>/', add_comment, name='add_comment'),
    re_path(r'^topics/(?P<slug>.+)/$', subtopic_list, name='subtopic_list'),

    # ВАЖНО: step_detail — САМЫЙ ПОСЛЕДНИЙ!!!
    re_path(r'^2/(?P<slug>.+)/$', step_detail2, name='step_detail2'),
    re_path(r'^(?P<slug>.+)/$', step_detail, name='step_detail'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]


