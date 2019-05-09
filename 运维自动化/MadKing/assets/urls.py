from django.urls import include, re_path
from assets import views

urlpatterns = [
    re_path(r'report/$', views.asset_report, name='asset_report'),
    re_path(r'report/asset_with_no_asset_id/$', views.asset_with_no_asset_id, name='acquire_asset_id'),
    re_path(r'^new_assets/approval/$', views.new_assets_approval, name="new_assets_approval"),

    # url(r'report/bulk_create/$',views.bulk_create_assets,name='bulk_create_assets' ),
    re_path(r'^report_test/$', views.asset_report_test),
    re_path(r'^acquire_asset_id_test/$', views.acquire_asset_id_test),
    re_path(r'^asset_list/$', views.asset_list, name="asset_list"),
    re_path(r'^asset_list/(\d+)/$', views.asset_detail, name="asset_detail"),
    re_path(r'^asset_list/list/$', views.get_asset_list, name="get_asset_list"),
    re_path(r'^asset_list/category/$', views.asset_category, name="asset_category"),
    re_path(r'^asset_event_logs/(\d+)/$', views.asset_event_logs, name="asset_event_logs"),
    re_path(r'^event_center/$', views.event_center, name="event_center")

]
