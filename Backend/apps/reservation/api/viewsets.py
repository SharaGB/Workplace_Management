from rest_framework.viewsets import ModelViewSet

from ..models import Desktop, Reservation

from .serializers import DesktopSerializer, ReservationSerializer

class DesktopViewset(ModelViewSet):
    queryset = Desktop.objects.all()
    serializer_class = DesktopSerializer
    
class ReservationViewset(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer