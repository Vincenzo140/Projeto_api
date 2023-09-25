from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from projetoApi.models.alunoModels import Aluno
from projetoApi.serializers.alunoSerializer import AlunoSerializer

class AlunoDetail(APIView):
    """
    Classe de visualização (view) para operações detalhadas em um aluno específico.

    A classe AlunoDetail fornece endpoints para recuperar, atualizar e excluir informações detalhadas de um aluno específico.

    Métodos:
    - get(request, pk): Retorna detalhes de um aluno específico com base no ID.
    - put(request, pk): Atualiza os detalhes de um aluno específico com base no ID.
    - delete(request, pk): Exclui um aluno específico com base no ID.

    Atributos:
    - model (Aluno): O modelo Aluno associado a esta visualização.
    - serializer_class (AlunoSerializer): O serializador usado para serializar e desserializar objetos Aluno.
    """
    
    def get(self, request, pk):
        """
        Retorna detalhes de um aluno específico com base no ID.

        Args:
        - request: A solicitação HTTP.
        - pk: O ID do aluno a ser recuperado.

        Retorna:
        - Response: Uma resposta HTTP contendo os detalhes do aluno em formato JSON.
        """
        aluno = Aluno.objects.get(pk=pk)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Atualiza os detalhes de um aluno específico com base no ID.

        Args:
        - request: A solicitação HTTP contendo os dados atualizados do aluno.
        - pk: O ID do aluno a ser atualizado.

        Retorna:
        - Response: Uma resposta HTTP com os detalhes do aluno atualizados em formato JSON, 
          ou uma resposta de erro 400 em caso de dados inválidos.
        """
        aluno = Aluno.objects.get(pk=pk)
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Exclui um aluno específico com base no ID.

        Args:
        - request: A solicitação HTTP.
        - pk: O ID do aluno a ser excluído.

        Retorna:
        - Response: Uma resposta HTTP com status 204 No Content para indicar que o aluno foi excluído com sucesso.
        """
        aluno = Aluno.objects.get(pk=pk)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
