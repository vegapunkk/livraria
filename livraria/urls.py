from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter

from uploader.router import router as uploader_router

from core.views import AutorViewSet, CategoriaViewSet, EditoraViewSet, LivroViewSet

router = DefaultRouter()
router.register(r"autores", AutorViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"livros", LivroViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
