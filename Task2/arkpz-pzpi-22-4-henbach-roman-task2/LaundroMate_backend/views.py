from rest_framework import viewsets, generics

from .models import User, Laundry, WashingMachine, WashingCycle, Payment, TimePricingCondition, \
    LoadPricingCondition, Stats
from .serializers import CustomerRegistrationSerializer, OwnerRegistrationSerializer, ManagerRegistrationSerializer, \
    UserSerializer, LaundrySerializer, WashingMachineSerializer, WashingCycleSerializer, PaymentSerializer, \
    TimePricingConditionSerializer, LoadPricingConditionSerializer, StatsSerializer


class CustomerRegistrationView(generics.CreateAPIView):
    serializer_class = CustomerRegistrationSerializer


class OwnerRegistrationView(generics.CreateAPIView):
    serializer_class = OwnerRegistrationSerializer


class ManagerRegistrationView(generics.CreateAPIView):
    serializer_class = ManagerRegistrationSerializer


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
        if getattr(self, 'swagger_fake_view', False):
            return Stats.objects.none()
        print(self.kwargs)
        return Stats.objects.filter(laundry_id=self.kwargs['laundry_id'])


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Payment.objects.none()
        return Payment.objects.filter(washing_cycle_id=self.kwargs['washing_cycle_id'])


class TimePricingConditionViewSet(viewsets.ModelViewSet):
    serializer_class = TimePricingConditionSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return TimePricingCondition.objects.none()
        return TimePricingCondition.objects.filter(laundry_id=self.kwargs['laundry_id'])


class LoadPricingConditionViewSet(viewsets.ModelViewSet):
    serializer_class = LoadPricingConditionSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return LoadPricingCondition.objects.none()
        return LoadPricingCondition.objects.filter(laundry_id=self.kwargs['laundry_id'])
