# Importações necessárias do Django REST framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from projetoApi.models.disciplinaModels import Disciplina
from projetoApi.serializers.disciplinaSerializer import DisciplinaSerializer

# Cria uma classe chamada DisciplinaList que herda de APIView
class DisciplinaList(APIView):
    # Método para lidar com solicitações GET
    def get(self, request):
        # Recupera todas as instâncias de Disciplina do banco de dados
        disciplinas = Disciplina.objects.all()
        # Serializa as instâncias de Disciplina em uma lista
        serializer = DisciplinaSerializer(disciplinas, many=True)
        # Retorna a resposta HTTP com os dados serializados
        return Response(serializer.data)

    # Método para lidar com solicitações POST
    def post(self, request):
        # Cria uma instância do DisciplinaSerializer com os dados da solicitação
        serializer = DisciplinaSerializer(data=request.data)
        # Verifica se a serialização é válida
        if serializer.is_valid():
            # Salva os dados no banco de dados
            serializer.save()
            # Retorna a resposta HTTP com os dados serializados e um status de criação (201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Se a serialização não for válida, retorna uma resposta com os erros de validação e um status de erro (400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
