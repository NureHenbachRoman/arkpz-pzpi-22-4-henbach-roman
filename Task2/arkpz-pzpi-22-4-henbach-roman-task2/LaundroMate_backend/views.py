from rest_framework import viewsets
from .models import User, Laundry, WashingMachine, WashingCycle, Booking, Payment, TimePricingCondition, \
    LoadPricingCondition, Stats
from .serializers import UserSerializer, LaundrySerializer, WashingMachineSerializer, WashingCycleSerializer, \
    BookingSerializer, PaymentSerializer, TimePricingConditionSerializer, LoadPricingConditionSerializer, \
    StatsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LaundryViewSet(viewsets.ModelViewSet):
    queryset = Laundry.objects.all()
    serializer_class = LaundrySerializer


class WashingMachineViewSet(viewsets.ModelViewSet):
    queryset = WashingMachine.objects.all()
    serializer_class = WashingMachineSerializer


class WashingCycleViewSet(viewsets.ModelViewSet):
    queryset = WashingCycle.objects.all()
    serializer_class = WashingCycleSerializer


class LaundryStatsViewSet(viewsets.ModelViewSet):
    serializer_class = StatsSerializer

    def get_queryset(self):
        return Stats.objects.filter(laundry_id=self.kwargs['laundry_pk'])


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class TimePricingConditionViewSet(viewsets.ModelViewSet):
    queryset = TimePricingCondition.objects.all()
    serializer_class = TimePricingConditionSerializer


class LoadPricingConditionViewSet(viewsets.ModelViewSet):
    queryset = LoadPricingCondition.objects.all()
    serializer_class = LoadPricingConditionSerializer
