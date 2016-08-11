from django.conf.urls import url, include
from django.contrib import admin

from .views import WelcomeView

admin.site.site_header = 'Big Money administration'

urlpatterns = [
    url(r'^$', WelcomeView.as_view(), name='welcome'),
    url(r'^api/', include('data.urls', namespace='api')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_docs.urls')),
]
