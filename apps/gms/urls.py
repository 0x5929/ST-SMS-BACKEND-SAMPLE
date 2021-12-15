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

router.register('cnaRotations', CNARotationView, basename='cnaRotations')
router.register('cnaStudents', CNAStudentView, basename='cnaStudents')
router.register('cnaTheoryRecords', CNATheoryRecordView,
                basename='cnaTheoryRecords')
router.register('cnaClinicalRecords', CNAClinicalRecordView,
                basename='cnaClinicalRecords')


router.register('hhaRotations', HHARotationView, basename='hhaRotations')
router.register('hhaStudents', HHAStudentView, basename='hhaStudents')
router.register('hhaTheoryRecords', HHATheoryRecordView,
                basename='hhaTheoryRecords')
router.register('hhaClinicalRecords', HHAClinicalRecordView,
                basename='hhaClinicalRecords')


urlpatterns = router.urls
