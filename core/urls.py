from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls', namespace='authentication')),

    path('api/', include('sms.urls', namespace='sms')),

    path('gsc/', include('google_sheet_connector.urls', namespace='gsc')),
]
