from .views import SchoolView, ProgramView, RotationView, StudentView
from rest_framework.routers import DefaultRouter

app_name = 'sms'

router = DefaultRouter()

router.register('schools', SchoolView, basename='schools')
router.register('programs', ProgramView, basename='programs')
router.register('rotations', ProgramView, basename='rotations')
router.register('students', StudentView, basename='students')

urlpatterns = router.urls
