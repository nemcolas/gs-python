pacientes = {}

def criar_paciente(nome, email):
    try:
        if nome not in pacientes:
            pacientes[nome] = {'email': email, 'exames': []}
            print(f'Paciente {nome} criado com sucesso.')
        else:
            print(f'O Paciente {nome} já existe.')
    except Exception as e:
        print(f"Erro ao criar paciente: {e}")

def salvar_exame(nome_paciente, dados_exame):
    try:
        if nome_paciente in pacientes:
            pacientes[nome_paciente]['exames'].append(dados_exame)
            print(f'Exame de {nome_paciente} salvo com sucesso.')
        else:
            print(f'O paciente {nome_paciente} não encontrado.')
    except Exception as e:
        print(f"Erro ao salvar exame: {e}")

def acessar_exame(nome_paciente):
    try:
        if nome_paciente in pacientes:
            if pacientes[nome_paciente]['exames']:
                ultimo_exame = pacientes[nome_paciente]['exames'][-1]
                print(f'Dados do último exame de {nome_paciente}: {ultimo_exame}')
            else:
                print(f'{nome_paciente} não tem exames registrados.')
        else:
            print(f'Paciente {nome_paciente} não encontrado.')
    except Exception as e:
        print(f"Erro ao acessar exame: {e}")

try:
    nome_usuario = input('Digite seu nome: ')
    email_usuario = input('Digite seu email: ')

    criar_paciente(nome_usuario, email_usuario)

    while True:
        dados_exame = input('Digite os dados do exame, ou escreva "sair" para finalizar o programa: ')

        if dados_exame.lower() == 'sair':
            break

        salvar_exame(nome_usuario, dados_exame)

    acessar_exame(nome_usuario)

except Exception as e:
    print(f"Erro geral: {e}")
