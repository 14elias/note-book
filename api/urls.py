from django.urls import path,include
from .views import DeleteNote, ListCreateNote

urlpatterns=[
    path('notes/',ListCreateNote.as_view(),name='create-list'),
    path('notes/delete/<int:pk>',DeleteNote.as_view(),name='delete-list')
]