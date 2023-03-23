from .models import Device, Connection
from rest_framework import serializers


class DeviceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
#    title = serializers.HyperlinkedRelatedField(view_name="Device", read_only=True, many=True)

    class Meta:
        model = Device
        fields = "__all__"


class ConnectionSerializer(serializers.ModelSerializer):
    device = serializers.StringRelatedField()

    class Meta:
        model = Connection
        fields = "__all__"
