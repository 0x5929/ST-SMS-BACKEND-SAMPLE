from django.urls import path
from django.views.generic.base import TemplateView
from .views import ImportFormView

app_name = 'gsc'

urlpatterns = [
    path('index.html', TemplateView.as_view(template_name='index.html')),
    path('import-csv/', ImportFormView.as_view(), name='import-csv'),
]
