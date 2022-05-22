from .views import SchoolView, ProgramView, RotationView, StudentView, GoogleSheetDataDumpView, StudentStatisticsView

from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = 'sms'

router = DefaultRouter()

router.register('schools', SchoolView, basename='schools')
router.register('programs', ProgramView, basename='programs')
router.register('rotations', RotationView, basename='rotations')
router.register('students', StudentView, basename='students')


urlpatterns = [
    # usage: http://127.0.0.1:8000/api/sms/google_sheet_datadump/?ssid=<spreadsheet id>&sid=<sheet id>&school_name=<school name value, ie: STI>
    path('google_sheet_datadump/', GoogleSheetDataDumpView.as_view()),

    # usage: http://127.0.0.1:8000/api/sms/student_statistics/
    path('student_statistics/', StudentStatisticsView.as_view()),
]

urlpatterns += router.urls
