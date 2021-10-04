from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),

    path('api/sms/', include('sms.urls', namespace='sms')),
    path('api/cms/', include('cms.urls', namespace='cms')),
    path('api/gms/', include('gms.urls', namespace='gms')),

    path('gsc/', include('google_sheet_connector.urls', namespace='gsc')),
]
