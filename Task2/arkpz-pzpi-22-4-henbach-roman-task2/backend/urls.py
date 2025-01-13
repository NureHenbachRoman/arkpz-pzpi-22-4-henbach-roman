from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from LaundroMate_backend import views
from LaundroMate_backend.schema import schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='Users')
router.register(r'laundries', views.LaundryViewSet)
router.register(r'laundries/(?P<laundry_id>[^/.]+)/stats', views.LaundryStatsViewSet, basename='laundry-stats')
router.register(
    r'laundries/(?P<laundry_id>[^/.]+)/time-pricing-conditions',
    views.TimePricingConditionViewSet,
    basename='time-pricing-conditions'
)
router.register(
    r'laundries/(?P<laundry_id>[^/.]+)/load-pricing-conditions',
    views.LoadPricingConditionViewSet,
    basename='load-pricing-conditions'
)
router.register(r'washing-machines', views.WashingMachineViewSet)
router.register(r'washing-cycles', views.WashingCycleViewSet)
router.register(r'washing-cycles/(?P<washing_cycle_id>[^/.]+)/payments', views.PaymentViewSet, basename='payments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/customer/', views.CustomerRegistrationView.as_view()),
    path('api/register/owner/', views.OwnerRegistrationView.as_view()),
    path('api/register/manager/', views.ManagerRegistrationView.as_view()),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh-token', TokenRefreshView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0))
]
