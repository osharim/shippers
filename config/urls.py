from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework_nested import routers

from sendengo.apps.catalog.views import CatalogViewSet, CatalogRequirementViewSet
from sendengo.apps.shippers.views import ShipperViewSet, ShipperRequirementViewSet
from sendengo.apps.carrier.views import CarrierViewSet, CarrierRequirementViewSet, CarrierViewShippersInComplianceViewSet

router = routers.SimpleRouter()

# Register Catalog API
router.register(r'catalog', CatalogViewSet, base_name='catalog')
catalog_router = routers.NestedSimpleRouter(router, r'catalog', lookup='catalog')
catalog_router.register(r'requirements', CatalogRequirementViewSet, base_name='requirements')


# Register Shipper API
router.register(r'shipper', ShipperViewSet, base_name='shipper')
shipper_router = routers.NestedSimpleRouter(router, r'shipper', lookup='shipper')
shipper_router.register(r'requirements', ShipperRequirementViewSet, base_name='requirements')

# Register Carrier API

router.register(r'carrier', CarrierViewSet, base_name='carrier')
carrier_router = routers.NestedSimpleRouter(router, r'carrier', lookup='carrier')
carrier_router.register(r'requirements', CarrierRequirementViewSet, base_name='requirements')

carrier_router.register(r'compliance', CarrierViewShippersInComplianceViewSet, base_name='compliance')

urlpatterns = [

    # Django JET URLS
    re_path(r'^jet/', include('jet.urls', 'jet')),

    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),

    # Basic routers
    re_path(r'^api/v1/', include(router.urls)),

    # Catalog routers
    re_path(r'^api/v1/', include(catalog_router.urls)),

    # Shipper routers
    re_path(r'^api/v1/', include(shipper_router.urls)),

    # Carrier routers
    re_path(r'^api/v1/', include(carrier_router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
