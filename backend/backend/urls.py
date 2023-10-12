from django.contrib import admin
from django.urls import path
from menu.views import DrinkAPIView
from loyalty.views import LoyaltyAPIView, CouponsAPIView 
from aboutCompany.views import LocationAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drinklist/', DrinkAPIView.as_view()),
    path('api/v1/loyaltylist/', LoyaltyAPIView.as_view()),
    path('api/v1/couponslist/', CouponsAPIView.as_view()),
    path('api/v1/locationlist/', LocationAPIView.as_view()),

]
