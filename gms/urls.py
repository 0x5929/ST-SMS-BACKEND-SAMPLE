from rest_framework.routers import DefaultRouter

from .views import \
    CNARotationView, \
    CNAStudentView, \
    CNATheoryRecordView, \
    CNAClinicalRecordView, \
    HHARotationView, \
    HHAStudentView, \
    HHATheoryRecordView, \
    HHAClinicalRecordView


app_name = 'gms'

router = DefaultRouter()

router.register('cnaRotation', CNARotationView, basename='cnaRotation')
router.register('cnaStudent', CNAStudentView, basename='cnaStudent')
router.register('cnaTheoryRecord', CNATheoryRecordView,
                basename='cnaTheoryRecord')
router.register('cnaClinicalRecord', CNAClinicalRecordView,
                basename='cnaClinicalRecord')


router.register('hhaRotation', HHARotationView, basename='hhaRotation')
router.register('hhaStudent', HHAStudentView, basename='hhaStudent')
router.register('hhaTheoryRecord', HHATheoryRecordView,
                basename='hhaTheoryRecord')
router.register('hhaClinicalRecord', HHAClinicalRecordView,
                basename='hhaClinicalRecord')


urlpatterns = router.urls
