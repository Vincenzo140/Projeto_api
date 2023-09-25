# Importação da classe AppConfig do Django
from django.apps import AppConfig

# Definição da classe AtividadesConfig que herda de AppConfig
class AtividadesConfig(AppConfig):
    # Configuração do campo de chave primária automática padrão (default_auto_field)
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Configuração do nome da aplicação
    name = 'projetoApi'
