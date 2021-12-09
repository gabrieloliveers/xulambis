import os
import ast
import json

def get_user() -> dict:
    user = {}
    user["nome"] = get_user_nome()
    user["data_nascimento"] = get_user_data_nascimento()
    user["email"] = get_user_email()
    user["senha"] = get_user_senha()
    insert_user(user)
    has_user(user)

#NOME DO USUÁRIO
def get_user_nome():
    nome = str(input('Digite seu nome: '))
    if len(nome) == 0:
        print('Não possui os caracteres necessários!')
        get_user_nome()
    elif len(nome) > 30:
        print('Nome excede 30 caracteres!')
        get_user_nome()
    return nome


#DATA DE NASCIMENTO DO USUÁRIO
def get_user_data_nascimento():
    data_nascimento = str(input('Data de nascimento: '))
    if len(data_nascimento) == 0:
        print('Não possui os caracteres necessários!')
        get_user_data_nascimento()
    elif len(data_nascimento) > 10:
        print('Data excede 10 caracteres!')
        get_user_data_nascimento()
    return data_nascimento      


#EMAIL DO USUÁRIO
def get_user_email():
    email = str(input('Digite seu email: '))
    if len(email) == 0:
        print('Email não possui os caracteres necessários!')
        get_user_email()
    elif len(email) > 30:
        print('Nome excede 30 caracteres!')
        get_user_email()
    return email

#SENHA DO USUÁRIO
def get_user_senha():
    senha = str(input('Digite sua senha: '))
    if len(senha) <= 7:
        print('Senha deve conter no mínimo 8 caracteres!')
        get_user_senha()
    elif len(senha) > 30:
        print('senha excede 30 caracteres!')
        get_user_senha()
    return senha

#INSERIR USUÁRIO
def insert_user(user):
    file = open("database.json", "a")
    file.write(json.dumps(user, ensure_ascii=False) + '\n') #pega um dict e transforma em json
    #file.write(str(user) + '\n')

#VALIDAR USUÁRIO
def has_user(user) -> bool:
    file = open("database.json", "r")
    for line in file:
        # database_user = ast.literal_eval(line) #ast.literal_eval transforma um str de volta para dict(dicionario)
        database_user = json.loads(line) # transforma um json em dicionario
        if database_user["email"] == user["email"]:
            return True
    return False