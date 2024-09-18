from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from tasks.views import RegisterView, TaskViewSet, user_detail


router = DefaultRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('users/<int:user_id>/', user_detail, name='user-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
