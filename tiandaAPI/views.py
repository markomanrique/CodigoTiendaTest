from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from tiandaAPI.models import Categoria
from tiandaAPI.serialyzers import CategoriaSerializer
from rest_framework import generics

# Create your views here.
class CategoriaList(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class= CategoriaSerializer
    queryset= Categoria.objects.all()
    
    