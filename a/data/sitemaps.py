from django.contrib.sitemaps import Sitemap
from django.utils.module_loading import import_string
from .abc import SUFFIX
SubtopicModel = import_string(f'data.models.Subtopic{SUFFIX}')
StepModel = import_string(f'data.models.Step{SUFFIX}')
class SubtopicSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6
    def items(self):
        return SubtopicModel.objects.all()
class StepSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    def items(self):
        return StepModel.objects.all()
    def lastmod(self, obj):
        return obj.updated_date
