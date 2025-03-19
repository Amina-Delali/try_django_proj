# example/views.py
from datetime import datetime
from django.shortcuts import render

from django.http import HttpResponse

from .serializers import *
from rest_framework import generics, authentication, permissions, status
from rest_framework.response import Response

# def index(request):
#     now = datetime.now()
#     html = f'''
#     <html>
#         <body>
#             <h1>Hello from Try Django 🧑‍💻</h1>
#             <p>The current time is { now }.</p>
#         </body>
#     </html>
#     '''
#     return HttpResponse(html)

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
def index(request):
    return render(request, 'notes/index.html')

# from django.contrib.auth.models import Group, User
# from rest_framework import permissions, viewsets

# from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all().order_by('name')
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
    
    
# class RegisterView(generics.CreateAPIView):
#     serializer_class = RegisterUserSerializer
#     permission_classes = (permissions.AllowAny,)
    
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({'user': UserSerializer(user, context= self.get_serializer_context()).data},
#                             status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)