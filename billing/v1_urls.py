from django.urls import include, path
from rest_framework import routers
from billing import v1_views

router = routers.DefaultRouter()
router.register(r'orders', v1_views.OrderViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
]
