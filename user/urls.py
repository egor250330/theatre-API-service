from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from user.views import CreateUserView, LoginUserView, ManageUserView

from rest_framework.authtoken import views

app_name = "user"

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("me/", ManageUserView.as_view(), name='me'),
]