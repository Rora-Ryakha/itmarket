"""
URL configuration for itmarket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from rest_framework import routers

# noinspection PyUnresolvedReferences
from publications.views import (CardViewSet, CardCommentViewSet, CardImageViewSet,
                                CardFileViewSet, CardCommentImageViewSet)

# noinspection PyUnresolvedReferences
from users.views import (UserViewSet, UserImageViewSet)

# tokens
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = routers.SimpleRouter()
router.register(r'cards/comments/images', CardCommentImageViewSet)
router.register(r'cards/comments', CardCommentViewSet)
router.register(r'cards/images', CardImageViewSet)
router.register(r'cards/files', CardFileViewSet)
router.register(r'cards', CardViewSet)
router.register(r'users/images', UserImageViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
    ]
