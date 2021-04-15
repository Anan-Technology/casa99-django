from django.conf.urls import url
from . import views
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as django_views

projects_urlpatterns = [
    url(r"^$", views.projects_index, name="projects")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
