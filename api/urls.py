from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, BillViewSet, ProductViewSet, BillProductViewSet, AuthViewSet

router = DefaultRouter()
router.register(r"clients", ClientViewSet)
router.register(r"bills", BillViewSet)
router.register(r"products", ProductViewSet)
router.register(r"billproducts", BillProductViewSet)
router.register(r"auth", AuthViewSet, basename="auth")

urlpatterns = [
    path("", include(router.urls)),
    path("billproducts/export_csv/", BillProductViewSet.as_view({"get": "export_csv"}), name="export_csv"),
    path("billproducts/bulk_create/", BillProductViewSet.as_view({"post": "bulk_create"}), name="bulk_create"),
    path("auth/login/", AuthViewSet.as_view({"post": "login"}), name="login"),
]