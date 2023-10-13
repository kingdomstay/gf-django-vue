from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from menu.views import DrinkViewSet, login_view
from loyalty.views import LoyaltyViewSet, CouponViewSet, login_view
from aboutCompany.views import LocationViewSet, login_view
from users.views import VisitorViewSet, login_view
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


SchemaView = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version="v1",
        description="API documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register(r"drink", DrinkViewSet)
router.register(r"loyalty", LoyaltyViewSet)
router.register(r"coupon", CouponViewSet)
router.register(r"location", LocationViewSet)
router.register(r"visitor", VisitorViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("login-view/", login_view),
    path("auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    # re_path("auth/", include("rest_framework_social_oauth2.urls"))
    # path("api/v1/loyaltylist/", LoyaltyAPIView.as_view()),
    # path("api/v1/couponslist/", CouponsAPIView.as_view()),
    # path("api/v1/locationlist/", LocationAPIView.as_view()),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
