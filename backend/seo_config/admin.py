from django.contrib import admin

from .models import SEO, RobotsTXT


@admin.register(RobotsTXT)
class RobotsTXTAdmin(admin.ModelAdmin):
    list_display = ("text",)


@admin.register(SEO)
class SEOAdmin(admin.ModelAdmin):
    list_display = (
        "slug",
        "title",
        "keywords",
        "lastmod",
        "priority",
        "changefreq",
    )
    search_fields = ("slug", "title", "keywords")
    list_editable = (
        "keywords",
        "priority",
        "changefreq",
    )
    save_on_top = True
    readonly_fields = ("lastmod",)  # только для чтения

    fieldsets = (
        ("Базовое", {"fields": ("slug", "title", "description", "keywords")}),
        ("Доп", {"fields": ("canonical_url", "noindex", "nofollow")}),
        (
            "Open Graph (соцсети)",
            {"fields": ("og_title", "og_description", "og_image")},
        ),
        (
            "Sitemap",
            {
                "fields": (
                    "priority",
                    "changefreq",
                    "lastmod",
                )  # lastmod останется, но будет readonly
            },
        ),
    )
