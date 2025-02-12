from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics

from api.models import Note 
from .serializer import NoteSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[AllowAny]

class ListCreateNote(generics.ListCreateAPIView):
    serializer_class=NoteSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else: 
            print(serializer.errors)
        return super().perform_create(serializer)

class DeleteNote(generics.DestroyAPIView):
    serializer_class=NoteSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)