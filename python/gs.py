pacientes = []

def criar_paciente(nome, email):
    if nome not in pacientes:
        pacientes[nome] = {'email': email, 'exames': []}
        print(f'Paciente {nome} criado com sucesso.')
    else:
        print(f'O Paciente {nome} já existe.')
