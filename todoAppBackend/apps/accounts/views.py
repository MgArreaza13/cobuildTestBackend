from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from apps.accounts import serializers as accounts_serializers
from apps.accounts import services as accounts_services
from django.utils.translation import gettext as _
from django.core.exceptions import PermissionDenied

# Create your views here.


class LoginView(APIView):
    """
       Get access to API with user information
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            user = accounts_services.login(request.data)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied as e:
            return Response({"detail": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        token, created = Token.objects.get_or_create(user=user)
        serializer = accounts_serializers.UserSerializers(user, many=False).data
        serializer['username'] = user.username
        serializer['token'] = token.key
        serializer['last_login'] = user.last_login
        return Response(serializer, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """
        Deletes the user's token in the system.
    """
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        try:
            user = accounts_services.logout(user=request.user)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied as e:
            return Response({"detail": str(e)}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'detail': str(_('You have disconnected from the system'))}, status=status.HTTP_200_OK)

