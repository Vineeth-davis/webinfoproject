# serializers.py
from rest_framework import serializers
from .models import Platform, Product,Device

class PlatformSerializer(serializers.ModelSerializer):
    modified_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Platform
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    modified_by = serializers.StringRelatedField(read_only=True)
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
        if not user.is_superuser and user.is_staff:
            # If the user is a technician, include the platform and product data

            data['product'] = {
                'id': instance.product.id,
                'platform': {
                    'id': instance.platform.id,
                    'name': instance.platform.name
                },
                'name': instance.product.name,
                'created_at': instance.product.created_at,
                'updated_at': instance.product.updated_at,
                'modified_by': instance.product.modified_by
            }
            data['platform'] = {
                'id': instance.platform.id,
                'name': instance.platform.name
            }
        if user.is_superuser:

            data['product'] = {
                'id': instance.product.id,
                'platform': {
                    'id': instance.platform.id,
                    'name': instance.platform.name
                },
                'name': instance.product.name,
                'created_at': instance.product.created_at,
                'updated_at': instance.product.updated_at,
                'modified_by': instance.product.modified_by
            }
            data['platform'] = {
                'id': instance.platform.id,
                'name': instance.platform.name
            }
        return data
