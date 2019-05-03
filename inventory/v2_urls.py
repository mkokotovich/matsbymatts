from django.urls import include, path
from rest_framework import routers
from inventory import v2_views

router = routers.DefaultRouter()
router.register(r'manufacturers', v2_views.ManufacturerViewSet)
router.register(r'items', v2_views.ItemViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
]
