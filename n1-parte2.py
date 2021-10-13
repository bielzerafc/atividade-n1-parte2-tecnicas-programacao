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
def main():
    op = 0
    while(op >= 0 and op <= 5):
        print("Digite 1 para cadastrar um novo usuário")
        print("Digite 2 para listar novos usuários")
        print("Digite 3 para buscar um usuário a partir de seu nome")
        print("Digite 4 para remover um usuário cadastrado buscando por seu e-mail.")
        print("Digite 5 para alterar o nome de um usuário buscando por seu e-mail") 
        print("Digite 6 para encerrar o programa\n")

        try:
            op = int(input())
        except:
            print("Insira um número de 1 a 6 para prosseguir.")
            continue

        if(op == 1):
            cadastrar()
        elif(op == 2):
            listagem = 0
            while listagem <=0 or listagem >=3:
                print("Digite 1 para listar os usuários em ordem de cadastro")
                print("Digite 2 para listar os usuários em ordem alfabética")

                listagem = int(input())

                if listagem == 1:
                    mostrarlista()
                elif listagem == 2:
                    mostrarlistaalfa()
                else:
                    print("Digite um número válido\n")

        elif(op == 3):
            buscarusuario(input("Insira o nome de um usuário para buscar seus dados "))
        elif(op == 4):
            deletarusuario(input("Insira o e-mail de um usuário para deletá-lo "))
        elif(op == 5):
            alterarnome(input("Insira o e-mail de um usuário para alterar seu nome "))

if __name__ == "__main__":
    main()

print("Lista de usuários: \n",lista)
