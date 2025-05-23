# Classe utilizada para facilitar a representação dos dados de um aluno em nosso programa
class Aluno:

	def __init__(self, ra, nome):
		self.__ra = ra
		self.__nome = nome
		self.__notas = []
	
	def adicionar_nota(self, nova_nota):
		self.__notas.append(nova_nota)
	
	def get_ra(self):
		return self.__ra
	
	def get_nome(self):
		return self.__nome
	
	def get_notas(self):
		return self.__notas   # retorna toda a lista de notas


# ==============================================
# Funções que lidam com os dados em arquivo (no disco):

def gravar_dados(nome_arquivo, lista_alunos):
	"""
	Recebe uma lista com objetos da classe Aluno e grava os dados de cada objeto em uma linha
	diferente do arquivo.
	"""
	with open(nome_arquivo, 'a') as arq:
		for aluno in lista_alunos:  # aluno é um objeto da classe Aluno
			ra = str(aluno.get_ra())  # converte o RA do aluno para string
			arq.write(ra)
			arq.write(';')
			arq.write(aluno.get_nome())
			notas = aluno.get_notas()   # o método get_notas() devolve a lista de notas 
			for nota in notas:
				arq.write(';')
				arq.write(str(nota))   # converte a nota para string e a escreve no arquivo
			arq.write('\n')

def ler_dados(nome_arquivo):
	"""
	Recebe o nome/caminho onde o arquivo se encontra no disco, lê cada linha do arquivo e as
	carrega na memória RAM como um objeto da classe Aluno.
	Ao final, retorna uma lista com objetos da classe Aluno.
	"""
	lista_alunos = []
	with open(nome_arquivo, 'r') as arq:
		for linha in arq:   # para cada linha contida no arquivo, faça:
			linha = linha.strip()  # remove o \n do final da linha (e também os espaços em branco)
			dados = linha.split(';')  # separa os dados contidos na linha com o separador ;
			ra = int(dados[0])
			nome = dados[1]
			novo_aluno = Aluno(ra, nome)
			for i in range(2, len(dados)):  # i varia de 2 até len(dados)-1
				nota = float(dados[i])
				novo_aluno.adicionar_nota(nota)
			lista_alunos.append(novo_aluno)
	return lista_alunos



# ==============================================
# Funções que lidam com os dados na memória RAM:

def gerar_lista_de_novos_alunos():
	"""
	Lê dados de novos alunos, e retorna uma lista onde cada elemento
	é um objeto da classe Aluno com os dados desses novos alunos.
	"""
	lista_alunos = []
	ra = int(input("\nInforme o novo RA (0 para parar): "))
	while ra > 0:  # enquanto o RA for diferente de -1, nós continuamos pegando dados de novos alunos
		nome = input("Informe o nome do aluno: ")
		novo_aluno = Aluno(ra, nome)
		qtd_notas = int(input("Informe quantas notas o aluno possui: "))
		for i in range(1, qtd_notas+1): # i vai variar de 1 até qtd_notas
			nota = float(input(f"Informe a {i}a nota: "))
			novo_aluno.adicionar_nota(nota)
		lista_alunos.append(novo_aluno)
		ra = int(input("\nInforme o novo RA (0 para parar): "))
	return lista_alunos


def imprimir_lista_de_alunos(lista_alunos):
	"""
	Recebe uma lista com objetos da classe Aluno e imprime os dados de todos os alunos.
	"""
	print('-'*60)
	for aluno in lista_alunos:
		print("RA:", aluno.get_ra())
		print("Nome:", aluno.get_nome())
		notas = aluno.get_notas()
		print("Notas:")
		for nota in notas:
			print(f"   {nota}")
		print('-'*60)


# Programa principal:
def main():
	nome_arquivo = "dados.csv"
	opcao = -1
	while opcao < 3:
		print("Escolha uma opção:")
		print("   1- Gravar novos alunos")
		print("   2- Listar os alunos gravados")
		print("   3- Sair do programa")
		opcao = int(input("Informe uma opção: "))
		if opcao == 1:
			lista_alunos = gerar_lista_de_novos_alunos()
			gravar_dados(nome_arquivo, lista_alunos)
		elif opcao == 2:
			lista_alunos = ler_dados(nome_arquivo)
			imprimir_lista_de_alunos(lista_alunos)

main()
