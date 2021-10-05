from rest_framework.routers import DefaultRouter

from .views import ClientView, NoteView


app_name = 'cms'

router = DefaultRouter()

router.register('clients', ClientView, basename='clients')
router.register('notes', NoteView, basename='notes')


urlpatterns = router.urls
