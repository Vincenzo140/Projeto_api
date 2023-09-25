from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from projetoApi.models.tarefaModels import Tarefa
from projetoApi.serializers.tarefaSerializer import TarefaSerializer

# Cria uma classe chamada TarefaListByAluno que herda de APIView
class TarefaListByAluno(APIView):
    def get(self, request, aluno_id):
        """
        Método para lidar com solicitações GET para recuperar todas as tarefas de um aluno específico.

        Args:
            request: A solicitação HTTP.
            aluno_id: O ID do aluno para o qual as tarefas devem ser recuperadas.

        Returns:
            Uma resposta HTTP com os dados de todas as tarefas do aluno serializados.
        """
        # Filtra as instâncias de Tarefa com base no ID do aluno fornecido
        tarefas = Tarefa.objects.filter(aluno__id=aluno_id)
        # Serializa as instâncias de Tarefa em uma lista
        serializer = TarefaSerializer(tarefas, many=True)
        # Retorna a resposta HTTP com os dados serializados
        return Response(serializer.data)
