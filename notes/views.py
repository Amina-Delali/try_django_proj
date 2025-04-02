# # # example/views.py
# # from datetime import datetime
# # from django.shortcuts import render

# # from django.http import HttpResponse

# # from .serializers import *
# # from rest_framework import generics, authentication, permissions, status
# # from rest_framework.response import Response

# # # def index(request):
# # #     now = datetime.now()
# # #     html = f'''
# # #     <html>
# # #         <body>
# # #             <h1>Hello from Try Django 🧑‍💻</h1>
# # #             <p>The current time is { now }.</p>
# # #         </body>
# # #     </html>
# # #     '''
# # #     return HttpResponse(html)

# # from django.contrib.auth.models import Group, User
# # from rest_framework import permissions, viewsets

# # from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


# # class UserViewSet(viewsets.ModelViewSet):
# #     """
# #     API endpoint that allows users to be viewed or edited.
# #     """
# #     queryset = User.objects.all().order_by('-date_joined')
# #     serializer_class = UserSerializer
# #     permission_classes = [permissions.IsAuthenticated]


# # class GroupViewSet(viewsets.ModelViewSet):
# #     """
# #     API endpoint that allows groups to be viewed or edited.
# #     """
# #     queryset = Group.objects.all().order_by('name')
# #     serializer_class = GroupSerializer
# #     permission_classes = [permissions.IsAuthenticated]
    
# # def index(request):
# #     return render(request, 'notes/index.html')

# # # from django.contrib.auth.models import Group, User
# # # from rest_framework import permissions, viewsets

# # # from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


# # # class UserViewSet(viewsets.ModelViewSet):
# # #     """
# # #     API endpoint that allows users to be viewed or edited.
# # #     """
# # #     queryset = User.objects.all().order_by('-date_joined')
# # #     serializer_class = UserSerializer
# # #     permission_classes = [permissions.IsAuthenticated]


# # # class GroupViewSet(viewsets.ModelViewSet):
# # #     """
# # #     API endpoint that allows groups to be viewed or edited.
# # #     """
# # #     queryset = Group.objects.all().order_by('name')
# # #     serializer_class = GroupSerializer
# # #     permission_classes = [permissions.IsAuthenticated]
    
    
# # # class RegisterView(generics.CreateAPIView):
# # #     serializer_class = RegisterUserSerializer
# # #     permission_classes = (permissions.AllowAny,)
    
# # #     def post(self, request, *args, **kwargs):
# # #         serializer = self.serializer_class(data=request.data)
# # #         if serializer.is_valid():
# # #             user = serializer.save()
# # #             return Response({'user': UserSerializer(user, context= self.get_serializer_context()).data},
# # #                             status=status.HTTP_201_CREATED)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import permissions
# from notes.models import Note
# from notes.serializers import NoteSerializer

# class NoteListApiView(APIView):
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]

#     # 1. List all
#     def get(self, request, *args, **kwargs):
#         '''
#         List all the note items for given requested user
#         '''
#         notes = Note.objects.filter(user = request.user.id)
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 2. Create
#     def post(self, request, *args, **kwargs):
#         '''
#         Create the Note with given note data
#         '''
#         data = {
#             'task': request.data.get('task'), 
#             'completed': request.data.get('completed'), 
#             'user': request.user.id
#         }
#         serializer = NoteSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class NoteDetailApiView(APIView):
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]

#     def get_object(self, note_id, user_id):
#         '''
#         Helper method to get the object with given note_id, and user_id
#         '''
#         try:
#             return Note.objects.get(id=note_id, user = user_id)
#         except Note.DoesNotExist:
#             return None

#     # 3. Retrieve
#     def get(self, request, note_id, *args, **kwargs):
#         '''
#         Retrieves the Note with given note_id
#         '''
#         note_instance = self.get_object(note_id, request.user.id)
#         if not note_instance:
#             return Response(
#                 {"res": "Object with note id does not exists"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         serializer = NoteSerializer(note_instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 4. Update
#     def put(self, request, note_id, *args, **kwargs):
#         '''
#         Updates the note item with given note_id if exists
#         '''
#         note_instance = self.get_object(note_id, request.user.id)
#         if not note_instance:
#             return Response(
#                 {"res": "Object with note id does not exists"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         data = {
#             'task': request.data.get('task'), 
#             'completed': request.data.get('completed'), 
#             'user': request.user.id
#         }
#         serializer = NoteSerializer(instance = note_instance, data=data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # 5. Delete
#     def delete(self, request, note_id, *args, **kwargs):
#         '''
#         Deletes the note item with given note_id if exists
#         '''
#         note_instance = self.get_object(note_id, request.user.id)
#         if not note_instance:
#             return Response(
#                 {"res": "Object with note id does not exists"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         note_instance.delete()
#         return Response(
#             {"res": "Object deleted!"},
#             status=status.HTTP_200_OK
#         )

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from notes.models import Note
from notes.serializers import NoteSerializer


from django.conf import settings
User = settings.AUTH_USER_MODEL




class NoteListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the note items for given requested user
        '''
        notes = Note.objects.filter(user = request.user.id)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Note with given note data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, note_id, user_id):
        '''
        Helper method to get the object with given note_id, and user_id
        '''
        try:
            return Note.objects.get(id=note_id, user = user_id)
        except Note.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, note_id, *args, **kwargs):
        '''
        Retrieves the Note with given note_id
        '''
        note_instance = self.get_object(note_id, request.user.id)
        if not note_instance:
            return Response(
                {"res": "Object with note id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = NoteSerializer(note_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, note_id, *args, **kwargs):
        '''
        Updates the note item with given note_id if exists
        '''
        note_instance = self.get_object(note_id, request.user.id)
        if not note_instance:
            return Response(
                {"res": "Object with note id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = NoteSerializer(instance = note_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, note_id, *args, **kwargs):
        '''
        Deletes the note item with given note_id if exists
        '''
        note_instance = self.get_object(note_id, request.user.id)
        if not note_instance:
            return Response(
                {"res": "Object with note id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        note_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
        
def index(request):
    return render(request, 'notes/index.html')        