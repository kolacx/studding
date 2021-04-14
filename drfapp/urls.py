from django.urls import path
from rest_framework.routers import SimpleRouter

from drfapp.views import RfModelView

router = SimpleRouter()

router.register(r'example1', RfModelView, basename='work')
router.register(r'example1/$', RfModelView, basename='work2')
# urlpatterns = router.urls

# urlpatterns = [
#     path('example/', RfViewSet.as_view({'get': 'list'}))
# ]

