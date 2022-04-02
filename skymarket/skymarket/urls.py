from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("redoc-tasks/", include("redoc.urls")),
    path("", include("users.urls")),
    path('', include("ads.urls")),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
