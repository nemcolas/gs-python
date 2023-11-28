pacientes = {}

def criar_paciente(nome, email):
    if nome not in pacientes:
        pacientes[nome] = {'email': email, 'exames': []}
        print(f'Paciente {nome} criado com sucesso.')
    else:
        print(f'O Paciente {nome} já existe.')

def salvar_exame(nome_paciente, dados_exame):
    if nome_paciente in pacientes:
        pacientes[nome_paciente]['exames'].append(dados_exame)
        print(f'Exame de{nome_paciente} salvo com sucesso.')
    else:
        print(f'O paciente {nome_paciente} não encontrado.')

def acessar_exame(nome_paciente):
    if nome_paciente in pacientes:
        if pacientes[nome_paciente]['exames']:
            ultimo_exame = pacientes[nome_paciente]['exames'][-1]
            print(f'Dados do último exame de {nome_paciente}: {ultimo_exame}')
        else:
            print(f'{nome_paciente} não tem exames registrados.')
    else:
        print(f'Paciente {nome_paciente} não encontrado.')



nome_usuario = input('Digite seu nome: ')
email_usuario = input('Digite seu email: ')

criar_paciente(nome_usuario, email_usuario)

dados_exame = input('Digite os dados do exame: ')
salvar_exame(nome_usuario, dados_exame)

acessar_exame(nome_usuario)