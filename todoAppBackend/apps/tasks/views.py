import json
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.tasks import services as tasks_services
from apps.tasks import serializers as tasks_serializers
# Create your views here.



class TasksView(APIView):

	"""
		get the list of tasks created by the user
	"""
	# permission_classes = (permissions.IsAuthenticated,)
	def get(self, request):
		try:
			tasks = tasks_services.get_list_tasks(request.user)
		except ValueError as e:
			return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
		except PermissionDenied as e:
			return Response({'detail': str(e)}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
			return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer = tasks_serializers.TasksSerializers(tasks, many=True).data
		return Response(serializer, status=status.HTTP_200_OK)