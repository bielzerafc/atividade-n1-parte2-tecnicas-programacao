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
        
def buscarusuario(nome):   #função para a opção 3
    for usuario in lista:
        if nome == usuario["nome"]:
            print("Nome: ", usuario["nome"], " E-mail: " , usuario["e-mail"])

def deletarusuario(email):   #função para a opção 4
    for dados in lista:
        if email == dados["e-mail"]:
            lista.remove(dados)
    for dados in dadoscadastro:
        quebra = dados.split(" ")
        if email == quebra[3]: 
            dadoscadastro.remove(dados)

def alterarnome(email):   #função para a opção 5
    novonome = input("Insira o novo nome do Usuario: ")
    for dados in lista:
        if email == dados["e-mail"]:
            dados["nome"] = novonome
    for dados in dadoscadastro:
        quebra = dados.split(" ")
        if email == quebra[3]:  
            dadoscadastro.remove(dados)
            novousuario = quebra
            novousuario[1] = novonome
            novousuario = novousuario[0] + " " + novousuario[1] + " " + novousuario[2] + " " + novousuario[3]
            dadoscadastro.append(novousuario)
