from aboutCompany.views import LocationViewSet, login_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from loyalty.views import CouponViewSet, login_view
from menu.views import DrinkViewSet, login_view
from rest_framework import permissions, routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from users.views import Profile, ProfileViewSet, login_view

SchemaView = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version="v1",
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register(r"drink", DrinkViewSet)
router.register(r"coupon", CouponViewSet)
router.register(r"location", LocationViewSet)
router.register(r"user", ProfileViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/drf-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("login-view/", login_view),
    path("auth/", include("djoser.urls")),
    re_path(r"auth/", include("djoser.urls.authtoken")),
    # re_path(r"auth/", include("rest_framework_social_oauth2.urls")),
    path(r"swagger/", SchemaView.with_ui("swagger", cache_timeout=0)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
