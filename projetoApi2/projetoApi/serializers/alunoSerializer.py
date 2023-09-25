from rest_framework import serializers
from projetoApi.models.alunoModels import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Aluno.

    O AlunoSerializer converte objetos Aluno em representações JSON e vice-versa.
    Ele é usado para serializar (converter em JSON) e desserializar (converter de JSON para objeto) instâncias do modelo Aluno.

    Atributos:
    - model (Aluno): O modelo Aluno associado a este serializador.
    - fields (list): Uma lista de campos a serem incluídos na serialização. 
      No caso de '__all__', todos os campos do modelo Aluno serão incluídos.

    Exemplo de uso:
    >>> aluno = Aluno.objects.get(pk=1)
    >>> serializer = AlunoSerializer(aluno)
    >>> serialized_data = serializer.data
    >>> print(serialized_data)
    {'id': 1, 'nome': 'Nome do Aluno', 'email': 'email@example.com'}
    """

    class Meta:
        """
        Classe Meta para configurar o serializador.
        """
        model = Aluno  # O modelo Aluno associado a este serializador.
        fields = '__all__'  # Inclui todos os campos do modelo Aluno na serialização.
