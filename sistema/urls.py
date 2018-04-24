from django.urls import path
from django.contrib import admin
from sistema.views import *

urlpatterns = [
	path('', index),
	path('login', login),
	path('alunos', alunos),
	path('atividades', atividades),
	path('detalhes_disciplinas', detalhes_disciplinas),
	path('nova_disciplina', nova_disciplina),
	path('admin/', admin.site.urls),
]