# _*_coding:utf-8_*_
from assets.myauth import UserProfile
from assets import models
from rest_framework import serializers


# 表现形式
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'token', 'is_staff', 'name', 'email')


class ServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Server
        fields = ('os_type', 'model', 'os_distribution')


class AssetSerializer(serializers.ModelSerializer):

    manufactory = serializers.HyperlinkedIdentityField(view_name="api:manufactory-detail",
                                                       lookup_field="id",
                                                       lookup_url_kwarg="pk")

    class Meta:
        model = models.Asset
        # depth = 1
        # fields = ('name', 'sn', 'networkdevice')
        fields = ('name', 'sn', 'manufactory', 'networkdevice')
        # extra_kwargs = {
        #     # 'server': {'view_name': 'api:servers', 'lookup_field': 'id'},
        # }


class ManufactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufactory
        fields = ('id', 'manufactory', 'support_num', 'memo')
