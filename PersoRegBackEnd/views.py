from rest_framework.response import Response
 
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework import status
 
from django.contrib.auth.models import User
 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import permissions
from custom_permissions import SpecialUserPermission

from django.contrib.auth import logout

  
# Create your views here.
class TestView(APIView):
	"""
	"""
 
	def get(self, request, format=None):
		return Response({'detail': "GET Response"})
 
	def post(self, request, format=None):
		try:
			data = request.DATA
		except ParseError as error:
			return Response(
				'Invalid JSON - {0}'.format(error.detail),
				status=status.HTTP_400_BAD_REQUEST
			)
		if "user" not in data or "password" not in data:
			return Response(
				'Wrong credentials',
				status=status.HTTP_401_UNAUTHORIZED
			)

		user = User.objects.first()
		if not user:
			return Response(
				'No default user, please create one',
				status=status.HTTP_404_NOT_FOUND
			)
		token = Token.objects.get_or_create(user=user)
		return Response({'detail': 'POST answer', 'token': token[0].key})

class AuthView(APIView):
	"""
	Authentication is needed for this methods
	"""
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		return Response({'detail': "I supongo you are authenticated"})



class TacView(APIView):
	"""
	Authentication is needed for this methods
	"""
	#authentication_classes = (TokenAuthentication,)
	#permission_classes = (SpecialUserPermission,)
 
	def get(self, request, format=None):
		usuario= User.objects.get(username=request.user.username)
		#usuario = User.objects.filter('user')
		tok = Token.objects.filter(user=usuario.id)
		#tok.delete()
		print tok[0].created
		#El token tendra una duracion de 2 horas
		return Response({'detail': "I suppose you are authenticated"})