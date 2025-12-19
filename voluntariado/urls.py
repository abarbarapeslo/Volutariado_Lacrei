from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profissionais.views import ProfissionalViewSet
from consultas.views import ConsultaViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from drf_spectacular.views import (SpectacularAPIView,SpectacularSwaggerView)


router = DefaultRouter()
router.register(r'profissionais', ProfissionalViewSet)
router.register(r'consultas', ConsultaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    #autenticação
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #documentação
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
