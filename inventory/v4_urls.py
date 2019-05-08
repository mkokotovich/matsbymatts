from django.urls import include, path
from rest_framework import routers
from inventory import v4_views

router = routers.DefaultRouter()
router.register(r'manufacturers', v4_views.ManufacturerViewSet)
router.register(r'items', v4_views.ItemViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
]
