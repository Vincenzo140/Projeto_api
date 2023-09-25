from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from projetoApi.models.disciplinaModels import Disciplina
from projetoApi.serializers.disciplinaSerializer import DisciplinaSerializer

# Cria uma classe chamada DisciplinaDetail que herda de APIView
class DisciplinaDetail(APIView):
    # Método para lidar com solicitações GET
    def get(self, request, pk):
        # Recupera uma instância da Disciplina com base no pk fornecido
        disciplina = Disciplina.objects.get(pk=pk)
        # Serializa a instância da Disciplina
        serializer = DisciplinaSerializer(disciplina)
        # Retorna a resposta HTTP com os dados serializados
        return Response(serializer.data)

    # Método para lidar com solicitações PUT
    def put(self, request, pk):
        # Recupera uma instância da Disciplina com base no pk fornecido
        disciplina = Disciplina.objects.get(pk=pk)
        # Cria uma instância do DisciplinaSerializer com os dados da solicitação
        serializer = DisciplinaSerializer(disciplina, data=request.data)
        # Verifica se a serialização é válida
        if serializer.is_valid():
            # Salva os dados atualizados no banco de dados
            serializer.save()
            # Retorna a resposta HTTP com os dados serializados
            return Response(serializer.data)
        # Se a serialização não for válida, retorna uma resposta com os erros de validação
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Método para lidar com solicitações DELETE
    def delete(self, request, pk):
        # Recupera uma instância da Disciplina com base no pk fornecido
        disciplina = Disciplina.objects.get(pk=pk)
        # Deleta a instância da Disciplina do banco de dados
        disciplina.delete()
        # Retorna uma resposta HTTP indicando que a exclusão foi bem-sucedida
        return Response(status=status.HTTP_204_NO_CONTENT)
