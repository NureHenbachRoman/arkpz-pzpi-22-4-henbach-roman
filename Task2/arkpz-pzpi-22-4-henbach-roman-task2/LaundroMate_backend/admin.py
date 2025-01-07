from django.contrib import admin
from .models import User, Laundry, WashingMachine, WashingCycle, Booking, Payment, TimePricingCondition, \
    LoadPricingCondition, Stats

admin.site.register(User)
admin.site.register(Laundry)
admin.site.register(WashingMachine)
admin.site.register(WashingCycle)
admin.site.register(Stats)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(TimePricingCondition)
admin.site.register(LoadPricingCondition)