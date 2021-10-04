from rest_framework.routers import DefaultRouter

from .views import CNARotationView, CNAStudentView, CNATheoryRecordView, CNAClinicalRecordView


app_name = 'gms'

router = DefaultRouter()

router.register('cnaRotation', CNARotationView, basename='cnaRotation')
router.register('cnaStudent', CNAStudentView, basename='cnaStudent')
router.register('cnaTheoryRecord', CNATheoryRecordView,
                basename='cnaTheoryRecord')
router.register('cnaClinicalRecord', CNAClinicalRecordView,
                basename='cnaClinicalRecord')


urlpatterns = router.urls
