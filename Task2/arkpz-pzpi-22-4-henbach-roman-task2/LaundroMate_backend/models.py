from django.contrib.auth.models import User
from django.db import models


class Laundry(models.Model):
    address = models.TextField()
    name = models.CharField(max_length=255)
    price_per_kg = models.DecimalField(max_digits=5, decimal_places=2)
    dynamic_pricing = models.BooleanField()
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_laundries')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_laundries')

    def __str__(self):
        return self.name


class WashingMachine(models.Model):
    class Status(models.TextChoices):
        available = 'available', 'Available'
        in_use = 'in_use', 'In Use'
        out_of_order = 'out_of_order', 'Out of Order'

    status = models.CharField(max_length=15, choices=Status.choices)
    max_load = models.DecimalField(max_digits=5, decimal_places=2)
    laundry = models.ForeignKey(Laundry, on_delete=models.CASCADE, related_name='washing_machines')

    def __str__(self):
        return f'{self.laundry.name} - {self.pk}'


class WashingCycle(models.Model):
    class Status(models.TextChoices):
        booked = 'booked', 'Booked'
        started = 'started', 'Started'
        in_progress = 'in_progress', 'In Progress'
        completed = 'completed', 'Completed'
        cancelled = 'cancelled', 'Cancelled'

    class Mode(models.TextChoices):
        delicate = 'delicate', 'Delicate'
        normal = 'normal', 'Normal'
        heavy = 'heavy', 'Heavy'

    class Temperature(models.IntegerChoices):
        cold = 0, 'Cold'
        warm = 30, 'Warm'
        hot = 60, 'Hot'

    mode = models.CharField(max_length=50, choices=Mode.choices)
    temperature = models.PositiveIntegerField(choices=Temperature.choices)
    status = models.CharField(max_length=15, choices=Status.choices)
    booked_for = models.DateTimeField(null=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    washing_machine = models.ForeignKey(WashingMachine, on_delete=models.CASCADE, related_name='washing_cycles')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='washing_cycles')

    def __str__(self):
        return f'{self.washing_machine} - {self.pk}'


class Stats(models.Model):
    """
    Stores the load percentage of a laundry at a given time.
    This is used to predict load percentage for future via linear regression model.
    """

    timestamp = models.DateTimeField()
    load_percentage = models.PositiveIntegerField()
    laundry = models.ForeignKey(Laundry, on_delete=models.CASCADE, related_name='stats')

    def __str__(self):
        return f'{self.laundry.name} - {self.pk} ({self.timestamp}, {self.load_percentage})'


class Payment(models.Model):
    class Status(models.TextChoices):
        pending = 'pending', 'Pending'
        completed = 'completed', 'Completed'
        failed = 'failed', 'Failed'

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField()
    status = models.CharField(max_length=15, choices=Status.choices)
    washing_cycle = models.ForeignKey(WashingCycle, on_delete=models.CASCADE, related_name='payments')

    def __str__(self):
        return f'{self.washing_cycle} - {self.pk} ({self.amount}, {self.time}, {self.status})'


class TimePricingCondition(models.Model):
    """
    Stores the price multiplier for a given time range. If dynamic pricing is enabled for a laundry,
    the multiplier will be applying to the base price of washing cycle during that time range.
    If ranges overlap, the one with the latest start time will be used.
    """

    start = models.TimeField()
    end = models.TimeField()
    price_multiplier = models.DecimalField(max_digits=5, decimal_places=2)
    laundry = models.ForeignKey(Laundry, on_delete=models.CASCADE, related_name='time_pricing_conditions')

    def __str__(self):
        return f'{self.laundry.name} - {self.pk} ({self.start}, {self.end}, {self.price_multiplier})'


class LoadPricingCondition(models.Model):
    """
    Stores the price multiplier for a given load percentage. If dynamic pricing is enabled for a laundry,
    the multiplier will be applied to the base price of washing cycle
    if load percentage is equal to the given percentage or higher.
    The one with the highest suitable load percentage will be used.
    """

    load_percentage = models.PositiveIntegerField()
    price_multiplier = models.DecimalField(max_digits=5, decimal_places=2)
    laundry = models.ForeignKey(Laundry, on_delete=models.CASCADE, related_name='load_pricing_conditions')

    def __str__(self):
        return f'{self.laundry.name} - {self.pk} ({self.load_percentage}, {self.price_multiplier})'
