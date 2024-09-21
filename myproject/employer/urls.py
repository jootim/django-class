from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    path("company-info/", views.companyinfoadd, name="company-info"),
    path("", include("core.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
