from rest_framework import serializers
from projetoApi.models.disciplinaModels import Disciplina

class DisciplinaSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Disciplina.

    O DisciplinaSerializer converte objetos Disciplina em representações JSON e vice-versa.
    Ele é usado para serializar (converter em JSON) e desserializar (converter de JSON para objeto) instâncias do modelo Disciplina.

    Atributos:
    - model (Disciplina): O modelo Disciplina associado a este serializador.
    - fields (list): Uma lista de campos a serem incluídos na serialização. 
      No caso de '__all__', todos os campos do modelo Disciplina serão incluídos.

    Exemplo de uso:
    >>> disciplina = Disciplina.objects.get(pk=1)
    >>> serializer = DisciplinaSerializer(disciplina)
    >>> serialized_data = serializer.data
    >>> print(serialized_data)
    {'id': 1, 'nome': 'Nome da Disciplina', 'descricao': 'Descrição da Disciplina'}
    """

    class Meta:
        """
        Classe Meta para configurar o serializador.
        """
        model = Disciplina  # O modelo Disciplina associado a este serializador.
        fields = '__all__'  # Inclui todos os campos do modelo Disciplina na serialização.
