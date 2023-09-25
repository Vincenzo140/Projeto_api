from django.db import models

class Aluno(models.Model):
    """
    Modelo para representar informações sobre alunos.
    """

    # Campo para armazenar o nome do aluno com um comprimento máximo de 255 caracteres.
    nome = models.CharField(max_length=255)

    # Campo para armazenar o email do aluno, que deve ser único.
    email = models.EmailField(unique=True)

    def __str__(self):
        """
        Retorna uma representação em string do objeto Aluno.

        Esta função é chamada quando você imprime um objeto Aluno ou o exibe em
        administração do Django.

        Exemplo de uso:
        >>> aluno = Aluno.objects.get(pk=1)
        >>> print(aluno)
        'Nome do Aluno'
        """
        return self.nome
