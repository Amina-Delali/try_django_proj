from django.apps import AppConfig

from django.conf import settings
User = settings.AUTH_USER_MODEL
class NotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notes'
