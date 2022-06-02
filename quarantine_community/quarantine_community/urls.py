"""quarantine_community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from quarantine_community import settings
from overview import views as oviews
from plaza import views as pviews

router = routers.DefaultRouter()
router.register(r'users', oviews.UserViewSet)
router.register(r'groups', oviews.GroupViewSet)
router.register(r'covid_basic_info', oviews.CovidBasicInfoViewSet)
router.register(r'supply_requests', pviews.SupplyRegistrationViewSet)
router.register(r'special_requests', pviews.SpecialRequestViewSet)
router.register(r'drinking_water_requests', pviews.DrinkingWaterRegistrationViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', view=include('overview.urls', namespace='overview')),
                  path('plaza/', view=include('plaza.urls', namespace='plaza')),
                  path('monitors/', view=include('monitors.urls', namespace='monitors')),
                  path('api/', include(router.urls)),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
