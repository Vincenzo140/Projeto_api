from django.db import models
from projetoApi.models.disciplinaModels import Disciplina
from projetoApi.models.alunoModels import Aluno

class Tarefa(models.Model):
    """
    Representa uma tarefa acadêmica atribuída a um aluno em um contexto educacional.

    A classe Tarefa inclui informações sobre o título, descrição, data de entrega,
    estado de conclusão, aluno responsável e disciplinas associadas.

    Atributos:
    - titulo (CharField): O título da tarefa, com até 255 caracteres.
    - descricao (TextField): Uma descrição mais detalhada da tarefa.
    - data_entrega (DateField): A data limite para a conclusão da tarefa.
    - concluida (BooleanField): Indica se a tarefa foi concluída (True) ou não (False).
    - aluno (ForeignKey para Aluno): O aluno atribuído à tarefa.
    - disciplinas (ManyToManyField para Disciplina): Disciplinas relacionadas à tarefa.

    Métodos:
    - __str__(): Retorna uma representação em texto da tarefa, usando o título como identificação única.

    Exemplo de uso:
    >>> tarefa = Tarefa.objects.get(pk=1)
    >>> print(tarefa)
    'Título da Tarefa'
    """
    # Campo para armazenar o título da tarefa com até 255 caracteres.
    titulo = models.CharField(max_length=255)

    # Campo para armazenar uma descrição mais detalhada da tarefa.
    descricao = models.TextField()

    # Campo para armazenar a data limite para a conclusão da tarefa.
    data_entrega = models.DateField()

    # Campo para indicar se a tarefa foi concluída ou não (por padrão, é False).
    concluida = models.BooleanField(default=False)

    # Relacionamento com o modelo Aluno (Many-to-One): Cada tarefa está associada a um aluno.
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    # Relacionamento com o modelo Disciplina (Many-to-Many): Uma tarefa pode estar relacionada a várias disciplinas.
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        """
        Retorna uma representação em texto da tarefa, usando o título como identificação única.

        Exemplo de uso:
        >>> tarefa = Tarefa.objects.get(pk=1)
        >>> print(tarefa)
        'Título da Tarefa'
        """
        return self.titulo
