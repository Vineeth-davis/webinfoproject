# serializers.py
from rest_framework import serializers
from .models import Platform, Product,Device

class PlatformSerializer(serializers.ModelSerializer):
    modified_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Platform
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        result = {
            'id': instance.id,
            'name': instance.name
        }

        return result


class ProductSerializer(serializers.ModelSerializer):
    modified_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        result = {
            'id': instance.id,
            'platform': {
                'id': instance.platform.id,
                'name': instance.platform.name
            },
            'name': instance.name,
            'created_at': instance.created_at,
            'updated_at': instance.updated_at,
            'modified_by': instance.modified_by.username
        }

        return result

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
    
'''
class DeviceSerializer(serializers.ModelSerializer):
    modified_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Device
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = self.context['request'].user

        result = {
            'id': instance.id,
            'product': {
                'id': instance.product.id,
                'platform': {
                    'id': instance.platform.id,
                    'name': instance.platform.name
                },
                'name': instance.product.name,
                'created_at': instance.product.created_at,
                'updated_at': instance.product.updated_at,
                'modified_by': instance.product.modified_by
            },
            'name': instance.name,
            'ipaddress': instance.ip_address,
            'type': instance.device_type,
            'username': instance.username
        }

        return result
