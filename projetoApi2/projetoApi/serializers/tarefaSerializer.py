from rest_framework import serializers
from projetoApi.models.tarefaModels import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Tarefa.

    O TarefaSerializer converte objetos Tarefa em representações JSON e vice-versa.
    Ele é usado para serializar (converter em JSON) e desserializar (converter de JSON para objeto) instâncias do modelo Tarefa.

    Atributos:
    - model (Tarefa): O modelo Tarefa associado a este serializador.
    - fields (list): Uma lista de campos a serem incluídos na serialização. 
      No caso de '__all__', todos os campos do modelo Tarefa serão incluídos.

    Exemplo de uso:
    >>> tarefa = Tarefa.objects.get(pk=1)
    >>> serializer = TarefaSerializer(tarefa)
    >>> serialized_data = serializer.data
    >>> print(serialized_data)
    {'id': 1, 'titulo': 'Título da Tarefa', 'descricao': 'Descrição da Tarefa', 'data_entrega': '2023-09-20', 'concluida': False, 'aluno': 1, 'disciplinas': [1, 2]}
    """

    class Meta:
        """
        Classe Meta para configurar o serializador.
        """
        model = Tarefa  # O modelo Tarefa associado a este serializador.
        fields = '__all__'  # Inclui todos os campos do modelo Tarefa na serialização.
