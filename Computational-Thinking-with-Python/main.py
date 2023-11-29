# importando as bibliotecas necessárias
import pandas as pd
import random
from datetime import datetime

cadastros = {
    "Nome do paciente":[],
    "CPF do paciente":[],
    "Email do paciente":[],
    "Senha do paciente":[],
    "Telefone do paciente":[]
}
prontuarios = {
    "Paciente":[],
    "Data de acesso":[],
    "Sintomas":[],
    "Medicamentos":[],
    "Alergias":[],
    "Doenças":[],
}
paciente = []

def cadastrar_paciente():
# criando inputs com nome, cpf, email, senha e telefone
    nome = input("Insira o nome do paciente")
    cpf = input("Insira o CPF do paciente")
    email = input("Insira o e-mail do paciente")
    senha = input("Insira a senha do paciente")
    telefone = input("Insira o telefone do paciente")
# criando estrutura if else que verifica se o cpf cadastrado já está contido no dicionário de cadastros
    if cpf not in cadastros["CPF do paciente"]:
# caso o cpf inserido não esteja contido no dicionário, adicione todos os inputs do usuário no dicionário        
        cadastros["Nome do paciente"].append(nome)
        cadastros["CPF do paciente"].append(cpf)
        cadastros["Email do paciente"].append(email)
        cadastros["Senha do paciente"].append(senha)
        cadastros["Telefone do paciente"].append(telefone)
# caso contrário, imprima uma mensagem indicando que o paciente já está cadastrado        
    else:
        print("\nEsse CPF já está cadastrado \n Faça o login para continuar")

def login_paciente():
    login = input("Digite o seu email")
    senha = input("Digite sua senha")
# caso o email e senha inseridos pelo paciente estejam cadastrados:
    if login in cadastros["Email do paciente"] and senha in cadastros["Senha do paciente"]:
# imprimindo uma mensagem que indica que o login foi um sucesso
        print("Login efetuado com sucesso!")
# salvando o indice do email do paciente em uma variável index         
        index = cadastros["Email do paciente"].index(login)
# salvando o nome que partilha o mesmo indice no dicionário cadastros na lista vazia paciente        
        paciente.append(cadastros["Nome do paciente"][index])
# imprimindo uma mensagem de boas vindas para o paciente        
        print(f"Bem vindo {paciente[0]}!")
# caso contrário:
    else:
# imprimindo a mensagem "Usuário ou Senha inválido."         
        print("Usuário ou Senha inválido.")  
def prontuario():
# usando biblioteca importada para salvar a data e hora em que foi preenchido o prontuário
    dia_e_horas = datetime.now()
    leitura_dia_e_horas = dia_e_horas.strftime("%d/%m/%Y %H:%M:%S")
# criando campos para que o paciente especifique os detalhes do prontuário
    sintomas = input("Quais sintomas você notou? Quando começaram os sintomas? Descreva de maneira detalhada")
    medicamentos = input("Faz uso de medicamentos? Se sim, quais?")
    alergias = input("Possui alergias? Se sim, quais?")
    doencas = input("Está fazendo tratamento de alguma doença? Se sim, quais?")
# adicionando os dados do prontuário ao dicionário prontuários    
    prontuarios["Paciente"].append(paciente_logado)
    prontuarios["Data de acesso"].append(leitura_dia_e_horas)
    prontuarios["Sintomas"].append(sintomas)
    prontuarios["Medicamentos"].append(medicamentos)
    prontuarios["Alergias"].append(alergias)
    prontuarios["Doenças"].append(doencas)        