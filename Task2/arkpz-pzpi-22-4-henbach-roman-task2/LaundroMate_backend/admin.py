from django.contrib import admin
from .models import Laundry, WashingMachine, WashingCycle, Payment, TimePricingCondition, \
    LoadPricingCondition, Stats

admin.site.register(Laundry)
admin.site.register(WashingMachine)
admin.site.register(WashingCycle)
admin.site.register(Stats)
admin.site.register(Payment)
admin.site.register(TimePricingCondition)
admin.site.register(LoadPricingCondition)
