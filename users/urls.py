from django.urls import re_path, path
from oauth2_provider import views as oauth2_views

import users.views as views
from .views import *


urlpatterns = [
    # re_path(r'^register/$', views.UserRegister.as_view()),
path('register/', RegisterView.as_view(), name='register'),

]