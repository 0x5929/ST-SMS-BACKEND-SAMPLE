from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from .views import GitPullView


env = getattr(settings, 'ENV')

admin_urls = 'dallas_cowboys_really_sucked_this_year_fkurwordl!st/' if env == 'PROD' else 'admin/'


urlpatterns = [
    
    path(f"{admin_urls}", admin.site.urls),

    # POST http://127.0.0.1:8000/auth/login/     BODY: {"email":"testsuper@localhost", "password": "xxxxx"}
    path('auth/', include('authentication.urls')),

    path('api/sms/', include('sms.urls', namespace='sms')),
    path('api/cms/', include('cms.urls', namespace='cms')),
    path('api/gms/', include('gms.urls', namespace='gms')),

    # CI/CD
    path('git_pull_main/', GitPullView.as_view()),
]

handler404 = 'core.errors.page_not_found_view'
handler500 = 'core.errors.server_error_view'