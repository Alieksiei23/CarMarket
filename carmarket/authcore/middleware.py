import jwt
from django.conf import settings
from django.http import JsonResponse
from rest_framework import status
from django.utils.deprecation import MiddlewareMixin


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return None

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

            request.is_staff = payload.get("is_staff")
            request.user_type = payload.get("user_type")
            request.user_id = payload.get("user_id")
            request.is_activated = payload.get("is_activated", False)

        except jwt.ExpiredSignatureError:
            return JsonResponse(
                {"error": "token is over"}, status=status.HTTP_401_UNAUTHORIZED
            )
        except jwt.InvalidTokenError:
            return JsonResponse(
                {"error": "token isn't correct"}, status=status.HTTP_401_UNAUTHORIZED
            )

        return None
