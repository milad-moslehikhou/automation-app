from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Automation App API",
      default_version='v1',
      description="",
      terms_of_service="",
      contact=openapi.Contact(email=""),
      license=openapi.License(name=""),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/actions/', include('action.api.urls', namespace="actions")),
    path('api/v1/reactions/', include('reaction.api.urls', namespace="reactions")),
    path('api/v1/tasks/', include('task.api.urls', namespace="tasks")),
    path('api/v1/executions/', include('execution.api.urls', namespace="executions")),
    path('api/v1/collector/', include('collector.api.urls', namespace="collector")),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('', RedirectView.as_view(url='admin/')),
]
