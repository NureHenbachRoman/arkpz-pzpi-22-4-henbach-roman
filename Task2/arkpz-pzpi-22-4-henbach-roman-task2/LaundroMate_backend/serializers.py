from rest_framework import serializers
from .enums import UserRole
from django.contrib.auth.models import User, Group
from .models import Laundry, WashingMachine, WashingCycle, Payment, TimePricingCondition, \
    LoadPricingCondition, Stats


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'groups']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class BaseRegistrationSerializer(serializers.ModelSerializer):
    role = None
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'groups']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        group = Group.objects.get(name=self.role.value)
        user.groups.add(group)
        return user


class CustomerRegistrationSerializer(BaseRegistrationSerializer):
    role = UserRole.CUSTOMER


class OwnerRegistrationSerializer(BaseRegistrationSerializer):
    role = UserRole.OWNER


class ManagerRegistrationSerializer(BaseRegistrationSerializer):
    role = UserRole.MANAGER


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
        extra_kwargs = {
            'laundry': {'read_only': True}
        }
        swagger_schema_fields = {
            'description': Stats.__doc__
        }

    def create(self, validated_data):
        laundry = Laundry.objects.get(pk=self.context['view'].kwargs['laundry_id'])
        validated_data['laundry'] = laundry
        return super().create(validated_data)

    def update(self, instance, validated_data):
        laundry = Laundry.objects.get(pk=self.context['view'].kwargs['laundry_id'])
        validated_data['laundry'] = laundry
        return super().update(instance, validated_data)


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        extra_kwargs = {
            'washing_cycle': {'read_only': True}
        }

    def create(self, validated_data):
        washing_cycle = WashingCycle.objects.get(pk=self.context['view'].kwargs['washing_cycle_id'])
        validated_data['washing_cycle'] = washing_cycle
        return super().create(validated_data)

    def update(self, instance, validated_data):
        washing_cycle = WashingCycle.objects.get(pk=self.context['view'].kwargs['washing_cycle_id'])
        validated_data['washing_cycle'] = washing_cycle
        return super().update(instance, validated_data)


class TimePricingConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimePricingCondition
        fields = '__all__'
        extra_kwargs = {
            'laundry': {'read_only': True}
        }
        swagger_schema_fields = {
            'description': TimePricingCondition.__doc__
        }

    def create(self, validated_data):
        laundry = Laundry.objects.get(pk=self.context['view'].kwargs['laundry_id'])
        validated_data['laundry'] = laundry
        return super().create(validated_data)

    def update(self, instance, validated_data):
        laundry = Laundry.objects.get(pk=self.context['view'].kwargs['laundry_id'])
        validated_data['laundry'] = laundry
        return super().update(instance, validated_data)


class LoadPricingConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadPricingCondition
        fields = '__all__'
        extra_kwargs = {
            'laundry': {'read_only': True}
        }
        swagger_schema_fields = {
            'description': LoadPricingCondition.__doc__
        }

    def create(self, validated_data):
        laundry = Laundry.objects.get(pk=self.context['view'].kwargs['laundry_id'])
        validated_data['laundry'] = laundry
        return super().create(validated_data)

    def update(self, instance, validated_data):
        laundry = Laundry.objects.get(pk=self.context['view'].kwargs['laundry_id'])
        validated_data['laundry'] = laundry
        return super().update(instance, validated_data)
