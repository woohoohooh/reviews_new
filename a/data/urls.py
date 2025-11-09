from django.urls import path, re_path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import (SubtopicSitemap, StepSitemap)
from . import views

sitemaps = {
    'subtopics': SubtopicSitemap,
    'steps': StepSitemap,
}

urlpatterns = [
    path('add/', views.add_step101, name='add_step101'),
    path('for_reviews_only/', views.create_step_for_reviews_only, name='create_step_for_reviews_only'),
    path('', views.index, name='index'),
    path('add-comment/<slug:step_slug>/', views.add_comment, name='add_comment'),
    re_path(rf'^topics/(?P<slug>.+)/$', views.subtopic_list, name='subtopic_list'),
    re_path(rf'^(?P<slug>.+)/$', views.step_detail, name='step_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
