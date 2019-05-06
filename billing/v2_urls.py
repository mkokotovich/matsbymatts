from django.urls import include, path
from rest_framework import routers
from billing import v2_views

router = routers.DefaultRouter()
router.register(r'orders', v2_views.OrderViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
]
