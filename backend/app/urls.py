from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # path("api/v1/auth/", include("users.urls")),
    # path("api/v1/seo/", include("seo.urls")),
    # path("api/v1/contacts/", include("contacts.urls")),
    # path("api/v1/salon/", include("salon.urls")),
    # path("api/v1/posts/", include("posts.urls")),
    # path("api/v1/products/", include("products.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


admin.site.site_header = "DV-FITNESS"
admin.site.site_title = "DV-FITNESS"
admin.site.index_title = "Моя админка"
