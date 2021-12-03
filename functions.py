import os
import ast
import json

def get_user_nome():
    nome = str(input('Digite seu nome: '))
    if len(nome) == 0:
        print('Não possui os caracteres necessários!')
        get_user_nome()
    elif len(nome) > 30:
        print('Nome excede 30 caracteres!')
        get_user_nome()
    return nome

def get_user() -> dict:
    user = {}
    user["nome"] = get_user_nome()

    # while True:
    #     if len(user['nome']) == 0:
    #         user['nome'] = str(input('Não possui os caracteres necessários ou excede (30)! Digite seu nome: '))
    #         breakpoint
    #     elif len(user['nome']) > 30:
    #         user['nome'] = str(input('Não possui os caracteres necessários ou excede (30)! Digite seu nome: '))
    #         breakpoint
    #     else:
    #         break

    user['data_nascimento'] = str(input('Data de nascimento: '))
    user['email'] = str(input('Digite seu email: '))
    user['senha'] = str(input('Digite sua senha: '))
    return user    
    
    #mudando qualquer coisa
    
    # DESAFIO 1: RESOLVER ESSE BUG! USEI ELSE: BREAKPOINT AONDE OBRIGA O USUÁRIO DIGITAR SEU NOME
    #PQ AO CONTRÁRIO DISSO O CADASTRO NÃO CONTINUA, AGORA MESMO ELE DIGITANDO E COLANCANDO OS 30 
    #CARACTERES QUE NÃO É PERMITIDO ELE TERA QUE COLOCAR A QUANTIDADE CORRETA, POIS SENÃO O CADASTRO
    #NÃO CONTINUA (PARCIALMENTE RESOLVIDO)

    # while len(user['nome']) == 0:
    #     user['nome'] = str(input('Nome não informado! Digite seu nome: '))
    # else:
    #     breakpoint    
    
    # while len(user['nome']) > 30:
    #     user['nome'] = str(input('Nome excede a quantidade de caracteres permitidos (30)! Digite seu nome: '))
    # else:
    #     breakpoint
    
    
    
    # DESAFIO 2: INSERIR CARACTERES ESPECIAIS NO JSON - ensure_ascii=False adicionado ao json.dumps
    # com esse comando o python escreve as próprias letras em vez de usar essa sequência que vem nele
    
def insert_user(user):
    file = open("database.json", "a")
    file.write(json.dumps(user, ensure_ascii=False) + '\n') #pega um dict e transforma em json
    #file.write(str(user) + '\n')

def has_user(user) -> bool:
    file = open("database.json", "r")
    for line in file:
        # database_user = ast.literal_eval(line) #ast.literal_eval transforma um str de volta para dict(dicionario)
        database_user = json.loads(line) # transforma um json em dicionario
        if database_user["email"] == user["email"]:
            return True
    return False