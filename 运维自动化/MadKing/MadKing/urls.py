from django.contrib import admin
from assets import rest_urls, urls as asset_urls
from MadKing import views
from django.urls import re_path, include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/', include((rest_urls, 'api'))),
    re_path('asset/', include((asset_urls, 'asset'))),
    re_path('/', views.index, name="dashboard"),
    re_path('login/', views.acc_login, name='login'),
]
