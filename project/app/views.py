#from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet
from .models import Platform,Product,Device
from .serializers import PlatformSerializer,ProductSerializer,DeviceSerializer
from .permissions import IsAdministrator,CanEditDevice,CanEditPlatform,CanEditProduct,IsTechnician

#@login_required()
class PlatformViewSet(ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = [IsAdministrator | CanEditPlatform]

#@login_required()
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdministrator | CanEditProduct]

#@login_required()
class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAdministrator | CanEditDevice]
