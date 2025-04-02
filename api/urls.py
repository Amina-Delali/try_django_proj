# """api URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# # from django.contrib import admin
# # from django.urls import path, include

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('', include('notes.urls')),
# # ]

# from django.urls import include, path
# from rest_framework import routers

# from notes import views
# from django.contrib import admin

# from django.conf.urls.static import static
# from django.conf import settings

# from notes import urls as notes_urls


# # router = routers.DefaultRouter()
# # router.register(r'users', views.UserViewSet)
# # router.register(r'groups', views.GroupViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('admin/', admin.site.urls),
#     path('api-auth/', include('rest_framework.urls')),
#     path('notes/', include(notes_urls))
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path, include
from notes import urls as notes_urls
from users import urls as users_urls


from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import include, path
from oauth2_provider import urls as oauth2_urls


# from django.contrib.auth.models import User, Group
# admin.autodiscover()

# from rest_framework import generics, permissions, serializers

# from oauth2_provider import urls as oauth2_urls
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', "first_name", "last_name")
#         extra_kwargs = {
#             'username': {'required': True}
#         }

# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ("name", )

# # Create the API views
# class UserList(generics.ListCreateAPIView):
#     # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
#     # permission_classes = [permissions.IsAuthenticated]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetails(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class GroupList(generics.ListAPIView):
#     permission_classes = [permissions.IsAuthenticated, TokenHasScope]
#     required_scopes = ['groups']
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
    
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include(oauth2_urls)),
    # path('users/', UserList.as_view()),
    # path('users/<pk>/', UserDetails.as_view()),
    # path('groups/', GroupList.as_view()),
    path('api-auth/',include(('rest_framework.urls'),namespace="auth")),
    path("accounts/", include("django.contrib.auth.urls")),

    path('notes/', include(notes_urls)),
    path(r'', include((notes_urls,"notes"), namespace="notes")),
    # path(r'users/', include((users_urls,"users"),namespace="users")),
    path('api/', include(('users.urls',"users"), namespace="users"))


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)