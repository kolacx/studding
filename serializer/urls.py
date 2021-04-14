from rest_framework.routers import SimpleRouter

from serializer.views import UsersView, PositionView, DepartamentView


router = SimpleRouter()

router.register(r'users', UsersView, basename='users')
# router.register(r'users/$', UsersView, basename='users')
router.register(r'position', PositionView, basename='positions')
router.register(r'departament', DepartamentView, basename='departaments')

urlpatterns = router.urls
