from django.urls import path
from .views import *

urlpatterns = [
    path('api/signup/', SignUpView.as_view(), name='signup'),
     path('api/signin/', SignInView.as_view(), name='signin'),
    path('api/v1/notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('api/v1/notes/<int:pk>/', NoteRetrieveUpdateDestroyView.as_view(), name='note-detail'),
]
