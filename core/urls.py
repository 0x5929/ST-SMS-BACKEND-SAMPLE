from django.contrib import admin
from django.conf import settings
from django.urls import path, include


env = getattr(settings, 'ENV')

admin_urls = 'dallas_cowboys_really_sucked_this_year_fkurwordl!st/' if env == 'prod' else 'admin/'


urlpatterns = [
    
    path(f"{admin_urls}", admin.site.urls),

    # POST http://127.0.0.1:8000/auth/login/     BODY: {"email":"testsuper@localhost", "password": "xxxxx"}
    path('auth/', include('authentication.urls')),

    path('api/sms/', include('sms.urls', namespace='sms')),
    path('api/cms/', include('cms.urls', namespace='cms')),
    path('api/gms/', include('gms.urls', namespace='gms')),

]

handler404 = 'core.views.page_not_found_view'
handler500 = 'core.views.server_error_view'