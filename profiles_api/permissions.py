from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
  """ Permite al usuario editar su propio perfil """

  def has_object_permission(self, request, view, obj):
    """ Revisar si el usuario está intentando editar su propio perfil """
    if request.method in permissions.SAFE_METHODS:
      return True

    return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
  """ Permite que el usuario actulice su propio status feed """
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    
    return obj.user_profile_id == request.user.id