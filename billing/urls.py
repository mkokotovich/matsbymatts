from django.urls import include, path
from rest_framework import routers
from billing import views

router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
]
