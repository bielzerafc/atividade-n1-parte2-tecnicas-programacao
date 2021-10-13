'''
Alunos:
Gabriel Ferreira Cavalhieri - RA: 21515695
João Lucas de Souza Yonéa - RA: 21598575
Roberta Ferreira Duprat - RA: 21551006
'''
lista = []
dadoscadastro = []

def cadastrar():  #função para a opção 1
    cadastro = {}
    cadastro["nome"] = input("Insira o nome do Usuário: ")
    cadastro["e-mail"] = input("Insira o e-mail do Usuário:")
    dadoscadastro.append("Nome: " + cadastro["nome"]  + " E-mail: " + cadastro["e-mail"])
    
    lista.append(cadastro)
    print("O usuário foi cadastrado com sucesso.\n")

def mostrarlista():   #função para a opção 2.1
    i = 0
    for usuario in lista:
        i = i + 1
        print(i , " - Nome: ", usuario["nome"], " E-mail: " , usuario["e-mail"])

def mostrarlistaalfa():   #função para a opção 2.2
    i = 0
    listaalfa = sorted(dadoscadastro)
    for listaemalfa in listaalfa:
        i = i + 1
        print(i ," - ", listaemalfa)
