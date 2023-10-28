from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Platform,Product,Device
from .serializers import PlatformSerializer,ProductSerializer,DeviceSerializer
from .permissions import AdminPlatformPermission, TechnicianPlatformPermission, AdminProductPermission, TechnicianProductPermission, AdminDevicePermission,TechnicianDevicePermission
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['POST'], permission_classes=[AdminPlatformPermission])
    def add_platform(self, request):
        # This action creates a new platform, which is the same as "add."
        return super().create(request)

    @action(detail=True, methods=['PUT'], permission_classes=[AdminPlatformPermission, TechnicianPlatformPermission])
    def edit_platform(self, request, pk=None):
        try:
            platform = self.queryset.get(pk=pk)
        except Platform.DoesNotExist:
            return Response({'error': 'Platform not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlatformSerializer(platform, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['DELETE'], permission_classes=[AdminPlatformPermission])
    def remove_platform(self, request, pk=None):
        try:
            platform = self.queryset.get(pk=pk)
        except Platform.DoesNotExist:
            return Response({'error': 'Platform not found.'}, status=status.HTTP_404_NOT_FOUND)

        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['POST'], permission_classes=[AdminProductPermission])
    def add_product(self, request):
        # This action creates a new product, which is the same as "add."
        return super().create(request)

    @action(detail=True, methods=['PUT'], permission_classes=[AdminProductPermission, TechnicianProductPermission])
    def edit_product(self, request, pk=None):
        try:
            product = self.queryset.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['DELETE'], permission_classes=[AdminProductPermission])
    def remove_product(self, request, pk=None):
        try:
            product = self.queryset.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['POST'], permission_classes=[AdminDevicePermission])
    def add_device(self, request):
        # This action creates a new device, which is the same as "add."
        return super().create(request)

    @action(detail=True, methods=['PUT'], permission_classes=[AdminDevicePermission, TechnicianDevicePermission])
    def edit_device(self, request, pk=None):
        try:
            device = self.queryset.get(pk=pk)
        except Device.DoesNotExist:
            return Response({'error': 'Device not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DeviceSerializer(device, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['DELETE'], permission_classes=[AdminDevicePermission])
    def remove_device(self, request, pk=None):
        try:
            device = self.queryset.get(pk=pk)
        except Device.DoesNotExist:
            return Response({'error': 'Device not found.'}, status=status.HTTP_404_NOT_FOUND)

        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
