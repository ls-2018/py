# _*_coding:utf-8_*_
from django.urls import re_path, include
from rest_framework import routers
from assets import rest_views as views
from assets import views as asset_views
from assets import rest_test

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('assets', views.AssetViewSet)
router.register('servers', views.ServerViewSet)
router.register('manufactory', views.ManuFactoryViewSet)

urlpatterns = [
    re_path('', include(router.urls)),
    re_path('asset_list/$', views.AssetList),
    re_path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path('dashboard_data/', asset_views.get_dashboard_data, name="get_dashboard_data"),
    re_path('eventlogs/$', rest_test.eventlog_list),
]
