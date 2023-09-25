# Importações necessárias do Django Admin
from django.contrib import admin
from projetoApi.models.alunoModels import Aluno
from projetoApi.models.tarefaModels import Tarefa
from projetoApi.models.disciplinaModels import Disciplina

# Registra os modelos Aluno, Tarefa e Disciplina no painel de administração do Django
admin.site.register(Aluno)  # Registra o modelo Aluno no admin
admin.site.register(Tarefa)  # Registra o modelo Tarefa no admin
admin.site.register(Disciplina)  # Registra o modelo Disciplina no admin
