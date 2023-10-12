"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
