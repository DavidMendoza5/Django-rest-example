from django.contrib import admin

from profiles_api import models

# Le da acceso al administrador para editar los modelos en la página de admin
admin.site.register([models.UserProfile, models.ProfileFeedItem])