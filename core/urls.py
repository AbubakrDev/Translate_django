from django.contrib import admin
from django.urls import path , include , re_path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
] + i18n_patterns(
    path('i18n/',include('django.conf.urls.i18n')),
    path('', include('translate.urls')),
    prefix_default_language = False,
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
