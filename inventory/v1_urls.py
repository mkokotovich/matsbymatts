from django.urls import include, path
from rest_framework import routers
from inventory import v1_views

router = routers.DefaultRouter()
router.register(r'manufacturers', v1_views.ManufacturerViewSet)
router.register(r'items', v1_views.ItemViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
]
