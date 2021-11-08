from .views import SchoolView, ProgramView, RotationView, StudentView, GoogleSheetDataDumpView

from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = 'sms'

router = DefaultRouter()

router.register('schools', SchoolView, basename='schools')
router.register('programs', ProgramView, basename='programs')
router.register('rotations', RotationView, basename='rotations')
router.register('students', StudentView, basename='students')


urlpatterns = [
    path('google_sheet_datadump/', GoogleSheetDataDumpView.as_view()),
]

urlpatterns += router.urls
