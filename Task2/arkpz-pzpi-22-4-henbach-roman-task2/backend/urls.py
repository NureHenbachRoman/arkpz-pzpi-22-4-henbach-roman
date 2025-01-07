from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from LaundroMate_backend import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'laundries', views.LaundryViewSet)
router.register(r'washing-machines', views.WashingMachineViewSet)
router.register(r'washing-cycles', views.WashingCycleViewSet)
router.register(r'bookings', views.BookingViewSet)
router.register(r'payments', views.PaymentViewSet)
router.register(r'time-pricing-conditions', views.TimePricingConditionViewSet)
router.register(r'load-pricing-conditions', views.LoadPricingConditionViewSet)

laundries_router = NestedDefaultRouter(router, r'laundries', lookup='laundry')
laundries_router.register(r'stats', views.LaundryStatsViewSet, basename='laundry-stats')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(laundries_router.urls)),
]
