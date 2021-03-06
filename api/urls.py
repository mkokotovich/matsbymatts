"""matsbymatts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/users/', include('users.urls')),
    url(r'^api/v1/inventory/', include('inventory.v1_urls')),
    url(r'^api/v2/inventory/', include('inventory.v2_urls')),
    url(r'^api/v3/inventory/', include('inventory.v3_urls')),
    url(r'^api/v4/inventory/', include('inventory.v4_urls')),
    url(r'^api/v1/billing/', include('billing.v1_urls')),
    url(r'^api/v2/billing/', include('billing.v2_urls')),
]
