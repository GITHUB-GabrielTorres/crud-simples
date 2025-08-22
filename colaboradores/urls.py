from django.urls import path
from .views import novo_colaborador, deletar_colaborador, editar_colaborador

urlpatterns = [
    path('novo/', novo_colaborador, name='novo_colaborador'),
    path('deletar/<int:id>', deletar_colaborador, name='deletar_colaborador'),
    path('editar/<int:id>', editar_colaborador, name='editar_colaborador')
]