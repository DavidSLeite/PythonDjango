from django.shortcuts import render

def index(request):
	return render(request, 'portal/index.html')
	
def login(request):
	if request.method == 'GET':
		return render(request, 'portal/login.html')
	else:
		print("Acesso Via POST")
		if request.POST.get('senha') == 'teste123':
			print("O Usuario", request.POST.get('email'), "entrou com sucesso")
			return render(request, 'portal/index.html')
		else:
			print("O Usuario", request.POST.get('email'), "Digitou a Senha errada")
			return render(request, 'portal/login.html')
	
def alunos(request):
	if request.method == 'GET':
		return render(request, 'portal/alunos.html')
	else:
		return render(request, 'portal/alunos.html')
		
def atividades(request):
	if request.method == 'GET':
		return render(request, 'portal/atividades.html')
	else:
		return render(request, 'portal/atividades.html')
		
def detalhes_disciplinas(request):
	if request.method == 'GET':
		return render(request, 'portal/detalhes_disciplinas.html')
	else:
		return render(request, 'portal/detalhes_disciplinas.html')
		
def nova_disciplina(request):
	if request.method == 'GET':
		return render(request, 'portal/nova_disciplina.html')
	else:
		return render(request, 'portal/nova_disciplina.html')
		