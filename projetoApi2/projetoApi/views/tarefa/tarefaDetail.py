from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from projetoApi.models.tarefaModels import Tarefa
from projetoApi.serializers.tarefaSerializer import TarefaSerializer

# Cria uma classe chamada TarefaDetail que herda de APIView
class TarefaDetail(APIView):
    def get(self, request, pk):
        """
        Método para lidar com solicitações GET para recuperar uma tarefa por ID.

        Args:
            request: A solicitação HTTP.
            pk: O ID da tarefa a ser recuperada.

        Returns:
            Uma resposta HTTP com os dados da tarefa serializados.
        """
        # Recupera uma instância de Tarefa com base no ID (pk) fornecido
        tarefa = Tarefa.objects.get(pk=pk)
        # Serializa a instância da Tarefa usando o TarefaSerializer
        serializer = TarefaSerializer(tarefa)
        # Retorna a resposta HTTP com os dados serializados
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Método para lidar com solicitações PUT para atualizar uma tarefa existente.

        Args:
            request: A solicitação HTTP com os dados a serem atualizados.
            pk: O ID da tarefa a ser atualizada.

        Returns:
            Uma resposta HTTP com os dados atualizados da tarefa serializados ou
            uma resposta de erro com status 400 se a validação falhar.
        """
        # Recupera uma instância de Tarefa com base no ID (pk) fornecido
        tarefa = Tarefa.objects.get(pk=pk)
        # Cria uma instância do TarefaSerializer com os dados da solicitação e a tarefa existente
        serializer = TarefaSerializer(tarefa, data=request.data)
        # Verifica se a serialização é válida
        if serializer.is_valid():
            # Salva os dados atualizados no banco de dados
            serializer.save()
            # Retorna a resposta HTTP com os dados serializados
            return Response(serializer.data)
        # Se a serialização não for válida, retorna uma resposta com os erros de validação e status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Método para lidar com solicitações DELETE para excluir uma tarefa existente.

        Args:
            request: A solicitação HTTP.
            pk: O ID da tarefa a ser excluída.

        Returns:
            Uma resposta HTTP com status 204 (No Content) para indicar que a exclusão foi bem-sucedida.
        """
        # Recupera uma instância de Tarefa com base no ID (pk) fornecido
        tarefa = Tarefa.objects.get(pk=pk)
        # Exclui a instância da Tarefa do banco de dados
        tarefa.delete()
        # Retorna uma resposta HTTP com status 204 (No Content) para indicar a exclusão bem-sucedida
        return Response(status=status.HTTP_204_NO_CONTENT)
