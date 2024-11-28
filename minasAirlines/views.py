# from django.shortcuts import render
from .serializers  import AirplaneSerializer, HangarSerializer, ListaAeronavesHangarSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Hangar, Airplane

# ViewSet para Hangar
class HangarViewSet(viewsets.ModelViewSet):
    queryset = Hangar.objects.all()
    serializer_class = HangarSerializer
    permission_classes = [IsAuthenticated]  # Exemplo de permissão para usuários autenticados

# ViewSet para Aeronave
class AeronaveViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_classes = [IsAuthenticated]  # Exemplo de permissão para usuários autenticados

#Exemplo de ListAPIView para listar aeronaves de um hangar específico
class ListaAeronavesHangar(generics.ListAPIView):
    serializer_class = AirplaneSerializer

    def get_queryset(self):
        # Obtém o ID do hangar da URL e filtra as aeronaves por hangar
        hangar_id = self.kwargs['pk']
        return Airplane.objects.filter(hangar_id=hangar_id)  # Filtra as aeronaves pelo hangar


        