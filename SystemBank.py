import random 
import os

banco = {
    "NomeDoBanco": "Santader",
    "agencia": "01",
    "Endereco": "Oscar Freire"
}

ContaDoCliente = {
    "Nome:": None,
    "ID": random.randint(1,1000),
    "Idade": None,
    "CPF": None,
    "Numero": None,
    "Saldo": None,
    "investimento":  {
        "cdb": None,
        "Fundos": None,
        "Bitcoin": None,
        "Etherium": None
    }

}



def adicionarCliente():
    print(f"""Seja bem vindo ao Banco {banco['NomeDoBanco']}, Agencia Número-{banco['agencia']}, localizada na {banco['Endereco']}.""")
    pass1 = input("Você deseja se cadastrar no nosso banco: ")
    if pass1 == "sim":
        os.system('cls')
        cadastroDoCliente()
    
    else:
        print("O que falta para criarmos uma conta aqui para você? ")
    




def cadastroDoCliente():
    print("""Obrigado pela preferencia em utilizar nosso banco
Agora farei umas perguntas básicas para o seu cadastro..""")
    
    print("-------------")
    nome = str (input("Qual o seu nome: "))
    ContaDoCliente["Nome:"] = nome
    os.system("cls")

    idade = int(input("Qual a sua idade: "))
    ContaDoCliente["Idade"] = idade
    os.system("cls")

    cpf = int(input("Qual seu CPF: "))
    ContaDoCliente["CPF"] = cpf
    os.system("cls")

    numero = int(input("Qual seu numero de contato: "))
    ContaDoCliente["Numero"] = numero
    os.system("cls")

    saldo = str(input("Deseja Adicionar seu saldo: "))
    if saldo == "sim":
        os.system("cls")
        adicionaSaldo()
    else:
        os.system("cls")
        painel()
   
def painel():
    print(f"Olá {ContaDoCliente['Nome:']}")
    print("=============")
    print("""a)cadastro
b)saldo
c)investimentos
d)emprestimo
""")
    print("=============")
    print("Para acessar uma das abas basta digitar a letra do diretório no input abaixo");
    escolhaLetra = input("Onde deseja acessar: ");
    if escolhaLetra == "a":
        os.system("cls")
        informacoesCliente();
    elif escolhaLetra == "b":
        os.system("cls")
        saldoCliente();
    elif escolhaLetra == "c":
        os.system("cls")
        investimentoCliente();
    elif escolhaLetra == "d":
        os.system("cls")
        emprestimo()
    else:
        print("caracter inválido")
        painel()


def informacoesCliente():
    print(f"""Olá {ContaDoCliente['Nome:']}
ID: {ContaDoCliente['ID']}
idade: {ContaDoCliente['Idade']}
CPF: {ContaDoCliente['CPF']}
numero: {ContaDoCliente['Numero']}

""")
    print("=================")
    voltarAoInicio = input("Digite 1 para voltar ao painel: ")
    if voltarAoInicio == "1":
        painel()
    
def saldoCliente():
    print(f"""Seu saldo atual é de
R${ContaDoCliente['Saldo']}""")
    print("=================")
    voltarAoInicio = input("Digite 1 para voltar ao painel: ")
    if voltarAoInicio == "1":
        os.system("cls")
        painel()
    

def investimentoCliente():
    ### print(f"Passarei a você agora uma tabela sobre seus investimentos {ContaDoCliente['investimento']}")

    print("=============================================")
    voltarAoInicio = input("Digite 1 para voltar ao painel: ")
    if voltarAoInicio == "1":
        painel()


def emprestimo():
    print("SEJA BEM VINDO A ABA DE EMPRESTIMO")
    print("=========================")
    valor = int(input(f"Com qual valor a gente pode te ajudar hoje {ContaDoCliente['Nome:']}: R$"))
    if valor == valor:
        aceite = input("Todos os nossos emprestimos tem 10% de juros, digite sim se entendeu: ")
        if aceite == "sim":
            print(F"O valor solicitado foi {valor}")
            valorDoEmprestimo = valor + (valor*10/100)
            print("===========")
            print(f"O valor total deu {valorDoEmprestimo} ")
            adicionaValorEmprestimo(valorDoEmprestimo)
            print("=================")
            print("Obrigado por confiar no nosso serviço")
            voltarAoInicio = input("Digite 1 para voltar ao painel: ")
            if voltarAoInicio == "1":
                painel()
        else:
            print("Ok, se você se interessar é só avisar")   
            print("===============")
            print("Obrigado por confiar no nosso serviço")
            voltarAoInicio = input("Digite 1 para voltar ao painel: ")
            if voltarAoInicio == "1":
                painel()         

def adicionaValorEmprestimo(valorDoEmprestimo):
    ContaDoCliente["Saldo"] = ContaDoCliente["Saldo"] + valorDoEmprestimo

def adicionaSaldo():
    valorAdicionado = int(input("Qual será o valor que será adicionado: "))
    ContaDoCliente["Saldo"] = valorAdicionado
    print("Obrigado, Seu dinheiro está seguro conosco")
    print("------------")
    saldoAtual = ContaDoCliente["Saldo"]
    print(f"Seu saldo atual é R${saldoAtual}")
    chamaInvestimento = input("""Nosso banco possui alguns ativos para investimento como
CriptoMoedas e cdb.
Você teria interesse em saber mais sobre nossos fundos: """)
    if chamaInvestimento == "sim":
        os.system("cls")
        clienteInvestimento()
    else:
        os.system("cls")
        print("Se você tiver interesse é só nos avisar passa te auxiliarmos")
        painel()


def clienteInvestimento():
    escolhaDeAtivo = input("Qual ativo você deseja escolher: ")
    if escolhaDeAtivo == "Cripto":
        os.system("cls")
        investimentoEmCripto()
    elif escolhaDeAtivo == "cdb":
        os.system("cls")
        cdb()
    else:
        print("ativo desconhecido, verifique se digitou corretamente")
        clienteInvestimento()
        

def cdb():
    print("No momento nosso CBD está com 110%.")
    print("--------------")
    valorInvestido = input("Quanto deseja investir: ")
    ContaDoCliente["investimento"[0]] = valorInvestido
    saldoDoCdb = ContaDoCliente["investimento"[0]]
    os.system("cls")
    print("Obrigado por confiar seu dinhero a nós")
    print("===========")
    print(f"Seu saldo atual no cdb é R${saldoDoCdb}")
    print("=================")
    print("Obrigado por confiar no nosso serviço")
    voltarAoInicio = input("Digite 1 para voltar ao painel: ")
    if voltarAoInicio == "1":
        painel()

def investimentoEmCripto():
    escolhaDeMoeda = input("""No momento nosso banco só tem suporte para
Bitcoin e Etherium, digite sim se você tem interesse em investir conosco: """)
    if escolhaDeMoeda == "sim":
        os.system("cls")
        qualMoeda = input("Em qual deseja investir, em Bitcoin ou Etherium: ")
        if qualMoeda == "Bitcoin":
            os.system("cls")
            investimentoEmBitcoin()
        elif qualMoeda == "Etherium":
            os.system("cls")
            investimentoEmEtherium()
        
    
def investimentoEmBitcoin():
    QuantidadeDeAtivo = input("O quanto desse ativo deseja comprar: ")
    os.system("cls")
    ContaDoCliente["investimento"[2]] = QuantidadeDeAtivo
    valorBitcoin = ContaDoCliente["investimento"[2]]
    print(f"O valor dá sua carteira Bitcoin é R${valorBitcoin}")
    print("=================")
    print("Obrigado por confiar no nosso serviço")
    voltarAoInicio = input("Digite 1 para voltar ao painel: ")
    if voltarAoInicio == "1":
        painel()


def investimentoEmEtherium():
    QuantidadeDeAtivo = input("O quanto desse ativo deseja comprar: ")
    ContaDoCliente["investimento"[3]] = QuantidadeDeAtivo
    valorEtherium = ContaDoCliente["investimento"[3]]
    print(f"O valor dá sua carteira Etherium é R${valorEtherium}")
    print("=================")
    print("Obrigado por confiar no nosso serviço")
    voltarAoInicio = input("Digite 1 para voltar ao painel: ")
    if voltarAoInicio == "1":
        painel()


adicionarCliente()
      


