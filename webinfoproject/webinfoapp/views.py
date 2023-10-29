from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Platform,Product,Device
from .serializers import PlatformSerializer,ProductSerializer,DeviceSerializer


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

    def create(self, request, *args, **kwargs):

        if request.user.is_superuser:
            return super().create(request, *args, **kwargs)
        else:
            return Response({'error': 'You do not have permission to add a platform.'},
                            status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()


        if request.user.is_superuser or request.user.is_staff:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response({'error': 'You do not have permission to edit this platform.'},
                            status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.is_superuser:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'You do not have permission to remove this platform.'},
                            status=status.HTTP_403_FORBIDDEN)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):

        if request.user.is_superuser:
            return super().create(request, *args, **kwargs)
        else:
            return Response({'error': 'You do not have permission to add a Product.'},
                            status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if request.user.is_superuser or request.user.is_staff:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response({'error': 'You do not have permission to edit this Product.'},
                            status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.is_superuser:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'You do not have permission to remove this Product.'},
                            status=status.HTTP_403_FORBIDDEN)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def create(self, request, *args, **kwargs):

        if request.user.is_superuser:
            return super().create(request, *args, **kwargs)
        else:
            return Response({'error': 'You do not have permission to add a Device.'},
                            status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if request.user.is_superuser:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        elif not request.user.is_superuser and request.user.is_staff:
            request_data = request.data.copy()
            if 'platform' in request_data:
                del request_data['platform']
            if 'product' in request_data:
                del request_data['product']
            serializer = self.get_serializer(instance, data=request_data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response({'error': 'You do not have permission to edit this Device.'},
                            status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.is_superuser:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'You do not have permission to remove this Device.'},
                            status=status.HTTP_403_FORBIDDEN)
'''
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

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
'''