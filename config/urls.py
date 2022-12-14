from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework.routers import DefaultRouter

from .schema import schema_view

router = DefaultRouter()


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('manage_api.facility.urls')),
    path('api/', include('manage_api.user.urls')),
    path('api/', include('manage_api.waste.urls')),
    path(settings.ADMIN_URL, admin.site.urls),
]

if settings.SWAGGER_ENABLED:
    urlpatterns += [
        re_path(
            r"swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
        path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
        path("swagger-auth/", include("rest_framework.urls", "swagger-auth")),
    ]

if settings.DEBUG:
    # https://docs.djangoproject.com/en/2.2/howto/static-files/#serving-files-uploaded-by-a-user-during-development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
