from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets, filters

from profiles_api import serializers, models, permissions

class HelloApiView(APIView):
  """ API View de prueba """
  serializer_class = serializers.HelloSerializer

  def get(self, request, format=None):
    """ Retornar lista de características del API View """
    an_apiview = [
      'Usamos métodos HTTP como funciones (get, post, patch, put, delete)',
      'Es similar a una vista tradicional de Django',
      'Mayor control sobre la lógica de nuestra aplicación',
      'Está mapeado manualmente a los URLs',
    ]

    # Response convierte la información a formato JSON, pero la información debe ser una lista o un diccionario
    return Response({
      'message': 'Hello',
      'an_apiview': an_apiview
    })
  
  def post(self, request):
    """ Crear un mensaje con nuestro nombre """
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}'
      
      return Response({
        'message': message
      })
    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
      )

  def put(self, request, pk=None):
    """ Maneja actualizar un objeto """
    return Response({
      'method': 'PUT',
    })

  def patch(self, request, pk=None):
    """ Maneja actualización parcial un objeto """
    return Response({
      'method': 'PATCH',
    })

  
  def delete(self, request, pk=None):
    """ Maneja eliminar un objeto """
    return Response({
      'method': 'DELETE',
    })

class HelloViewSet(viewsets.ViewSet):
  """ ViewSet de prueba """

  def list(self, request):
    a_viewset = [
      'Usa acciones (list, create, retrieve, update, partial_update)',
      'Automáticamente mapea a los URLs usando routers',
      'Provee más funcionalidad con menos código'
    ]

    return Response({
      'message': 'Hola',
      'a_viewset': a_viewset
    })

class UserProfileViewSet(viewsets.ModelViewSet):
  """ Crear y actualizar perfiles """
  serializer_class = serializers.UserProfileSerializer
  queryset = models.UserProfile.objects.all()
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.UpdateOwnProfile,)
  
  # Agregar filtros
  filter_backends = (filters.SearchFilter,)
  search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
  """ Clase que se encarga de crear los tokens de autenticación """
  renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
  """ Maneja el crear, leer y actualizar el profile feed """
  authentication_classes = (TokenAuthentication,)
  serializer_class = serializers.ProfileFeedItemSerializer
  queryset = models.ProfileFeedItem.objects.all()
  permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

  def perform_create(self, serializer):
    """ Setea el perfil de usuario para el usuario que está loggeado """
    serializer.save(user_profile=self.request.user)