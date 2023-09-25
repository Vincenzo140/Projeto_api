from django.db import models

class Disciplina(models.Model):
    """
    Modelo para representar informações sobre disciplinas.

    Este modelo define os campos e métodos relacionados às disciplinas de um sistema acadêmico.
    Cada disciplina é identificada por um nome único e pode ter uma descrição opcional.

    Exemplo de uso:
    >>> disciplina = Disciplina.objects.get(pk=1)
    >>> print(disciplina)
    'Nome da Disciplina'
    """

    # Campo para armazenar o nome da disciplina com um comprimento máximo de 255 caracteres.
    nome = models.CharField(max_length=255)

    # Campo para armazenar a descrição da disciplina como um texto longo.
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Retorna uma representação em string do objeto Disciplina.

        Esta função é chamada quando você imprime um objeto Disciplina ou o exibe em
        administração do Django.

        Exemplo de uso:
        >>> disciplina = Disciplina.objects.get(pk=1)
        >>> print(disciplina)
        'Nome da Disciplina'
        """
        return self.nome
