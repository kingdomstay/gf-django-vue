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
    path("api/", include(router.urls)),
    path("login-view/", login_view),
    path("auth/", include("djoser.urls")),
    # path(r"^account/", include("users.urls")),
    re_path(r"auth/", include("djoser.urls.authtoken")),
    path(r"swagger/", SchemaView.with_ui("swagger", cache_timeout=0)),
    # url(r'^edit/$', views.edit, name='edit'),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
