from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from projetoApi.models.alunoModels import Aluno
from projetoApi.serializers.alunoSerializer import AlunoSerializer

class AlunoList(APIView):
    """
    Uma classe de visualização para operações de listagem e criação de alunos.

    A classe AlunoList fornece endpoints para listar todos os alunos e criar um novo aluno.

    Métodos:
    - get(request): Retorna a lista de todos os alunos.
    - post(request): Permite a criação de um novo aluno.

    Atributos:
    - model (Aluno): O modelo Aluno associado a esta visualização.
    - serializer_class (AlunoSerializer): O serializador usado para serializar e desserializar objetos Aluno.
    """
    
    def get(self, request):
        """
        Retorna a lista de todos os alunos.

        Args:
        - request: A solicitação HTTP.

        Retorna:
        - Response: Uma resposta HTTP contendo a lista de alunos em formato JSON.
        """
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Permite a criação de um novo aluno.

        Args:
        - request: A solicitação HTTP contendo os dados do novo aluno a ser criado.

        Retorna:
        - Response: Uma resposta HTTP com os detalhes do novo aluno criado em formato JSON, 
          ou uma resposta de erro 400 em caso de dados inválidos.
        """
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
