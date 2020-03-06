from rest_framework import routers
from .api import NotaViewSet

router = routers.DefaultRouter()
router.register('api/note', NotaViewSet, 'note')

urlpatterns = router.urls
