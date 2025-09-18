from django.contrib.sitemaps import Sitemap

from seo_config.models import SEO


class SEOSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return SEO.objects.all()

    def location(self, obj):
        return f"/{obj.slug}/" if obj.slug != "home" else "/"

    def lastmod(self, obj):
        return obj.lastmod or obj.updated_at

    def changefreq(self, obj):
        return obj.changefreq

    def priority(self, obj):
        return float(obj.priority)

    def get_urls(self, page=1, site=None, protocol=None):
        """
        Переопределяем, чтобы всегда было https://
        """
        return super().get_urls(page=page, site=site, protocol="https")
