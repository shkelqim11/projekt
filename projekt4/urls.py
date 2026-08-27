from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from rezervime.views import kontakt

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("rezervime.urls")),

    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("sherbimet.html", TemplateView.as_view(template_name="sherbimet.html")),
    path("rreth-nesh.html", TemplateView.as_view(template_name="rreth-nesh.html")),
    path("kontakt/", kontakt, name="kontakt"),
    path("kontakt.html", kontakt, name="kontakt-page"),
]

if settings.DEBUG:
    urlpatterns += static("/", document_root=settings.STATICFILES_DIRS[0])