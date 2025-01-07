from rest_framework import serializers
from .models import User, Laundry, WashingMachine, WashingCycle, Booking, Payment, TimePricingCondition, \
    LoadPricingCondition, Stats


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class LaundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laundry
        fields = '__all__'


class WashingMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = WashingMachine
        fields = '__all__'


class WashingCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WashingCycle
        fields = '__all__'


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class TimePricingConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimePricingCondition
        fields = '__all__'


class LoadPricingConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadPricingCondition
        fields = '__all__'
