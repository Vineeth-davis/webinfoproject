# serializers.py
from rest_framework import serializers
from .models import Platform, Product,Device

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

'''
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        
        if user.is_technican:
            fields = '__all__'
            read_only_fields = ('platform','product')
        else:
            fields = '__all__'

'''

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = self.context['request'].user
        if not user.is_superuser and user.is_staff:
            data['platform'] = instance.platform.name if instance.platform else None
            data['product'] = instance.product.name if instance.product else None
        return data