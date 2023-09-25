# Importações necessárias do Django
from django.urls import path, include

# Importações das visualizações (views) relacionadas aos alunos, disciplinas e tarefas
from projetoApi.views.aluno.alunoList import AlunoList
from projetoApi.views.aluno.alunoDetail import AlunoDetail
from projetoApi.views.disciplina.disciplinaList import DisciplinaList
from projetoApi.views.disciplina.disciplinaDetail import DisciplinaDetail
from projetoApi.views.tarefa.tarefaList import TarefaList
from projetoApi.views.tarefa.tarefaDetail import TarefaDetail
from projetoApi.views.tarefa.tarefaListByAluno import TarefaListByAluno

# Lista de URLs (urlpatterns) para as visualizações da API
urlpatterns = [
    # URLs para as visualizações relacionadas aos alunos
    path('alunos/', AlunoList.as_view(), name='aluno-list'),  # Lista de todos os alunos
    path('alunos/<int:id>/', AlunoDetail.as_view(), name='aluno-detail'),  # Detalhes de um aluno específico

    # URLs para as visualizações relacionadas às disciplinas
    path('disciplinas/', DisciplinaList.as_view(), name='disciplina-list'),  # Lista de todas as disciplinas
    path('disciplinas/<int:id>/', DisciplinaDetail.as_view(), name='disciplina-detail'),  # Detalhes de uma disciplina específica

    # URLs para as visualizações relacionadas às tarefas
    path('tarefas/', TarefaList.as_view(), name='tarefa-list'),  # Lista de todas as tarefas
    path('tarefas/<int:id>/', TarefaDetail.as_view(), name='tarefa-detail'),  # Detalhes de uma tarefa específica

    # URL para listar as tarefas de um aluno específico
    path('alunos/<int:aluno_id>/tarefas/', TarefaListByAluno.as_view(), name='tarefa-list-by-aluno'),
]
