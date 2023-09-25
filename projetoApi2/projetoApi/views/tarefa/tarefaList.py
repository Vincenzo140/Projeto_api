from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from projetoApi.models.tarefaModels import Tarefa
from projetoApi.serializers.tarefaSerializer import TarefaSerializer

# Cria uma classe chamada TarefaList que herda de APIView
class TarefaList(APIView):
    def get(self, request):
        """
        Método para lidar com solicitações GET para recuperar todas as tarefas.

        Args:
            request: A solicitação HTTP.

        Returns:
            Uma resposta HTTP com os dados de todas as tarefas serializados.
        """
        # Recupera todas as instâncias de Tarefa do banco de dados
        tarefas = Tarefa.objects.all()
        # Serializa as instâncias de Tarefa em uma lista
        serializer = TarefaSerializer(tarefas, many=True)
        # Retorna a resposta HTTP com os dados serializados
        return Response(serializer.data)

    def post(self, request):
        """
        Método para lidar com solicitações POST para criar uma nova tarefa.

        Args:
            request: A solicitação HTTP com os dados da nova tarefa a ser criada.

        Returns:
            Uma resposta HTTP com os dados da tarefa criada serializados e status 201 (Created)
            ou uma resposta de erro com status 400 se a validação falhar.
        """
        # Cria uma instância do TarefaSerializer com os dados da solicitação
        serializer = TarefaSerializer(data=request.data)
        # Verifica se a serialização é válida
        if serializer.is_valid():
            # Salva os dados da nova tarefa no banco de dados
            serializer.save()
            # Retorna a resposta HTTP com os dados serializados e status 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Se a serialização não for válida, retorna uma resposta com os erros de validação e status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
