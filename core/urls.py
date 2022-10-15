from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # POST http://127.0.0.1:8000/auth/login/     BODY: {"email":"testsuper@localhost", "password": "xxxxx"}
    path('auth/', include('authentication.urls')),

    path('api/sms/', include('sms.urls', namespace='sms')),
    path('api/cms/', include('cms.urls', namespace='cms')),
    path('api/gms/', include('gms.urls', namespace='gms')),
]
