# notes/urls.py
from django.urls import path


from notes.views import index

urlpatterns = [
    path('', index),
]