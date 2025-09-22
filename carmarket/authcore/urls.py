from django.urls import path, include
from rest_framework_simplejwt.views import  TokenRefreshView, TokenVerifyView

from authcore.views import CustomTokenObtainPairView



urlpatterns = [
    path('', include('djoser.urls')),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]