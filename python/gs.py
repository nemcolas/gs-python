pacientes = []

def criar_paciente(nome, email):
    if nome not in pacientes:
        pacientes[nome] = {'email': email, 'exames': []}
        print(f'Paciente {nome} criado com sucesso.')
    else:
        print(f'O Paciente {nome} já existe.')

def enviar_exame(nome_paciente, dados_exame):
    if nome_paciente in pacientes:
        pacientes[nome_paciente]['exames'].append(dados_exame)
        print(f'Exame enviado para {nome_paciente} com sucesso.')
    else:
        print(f'O paciente {nome_paciente} não encontrado.')
