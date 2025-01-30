from faker import Faker
from random import Random

fake = Faker('pt-BR')
fake.seed_instance(0)
rng = Random(0)

estados = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF',
    'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA',
    'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS',
    'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
]

profissoes = [
    ('Médico', True),
    ('Enfermeiro', False),
    ('Dentista', True),
    ('Psicólogo', False),
    ('Farmacêutico', True),
    ('Fisioterapeuta', True),
    ('Nutricionista', False),
    ('Terapeuta Ocupacional', True),
    ('Fonoaudiólogo', True),
    ('Biomédico', False),
    ('Técnico de Enfermagem', False),
    ('Assistente Social', False),
    ('Educador Físico', False),
    ('Veterinário', True),
    ('Ortopedista', True)
]

def crm():
    return 'CRM/' + rng.choice(estados) + ' ' + str(rng.randint(0, 999999)).zfill(6)

print('INSERT INTO ProfissionalSaude')
print('(CodProfissional, CRM, NomeSocial, NomeCivil, Profissao)')
print('VALUES')
quantidade_profissionais_saude = 30
for i in range(quantidade_profissionais_saude):
    prof, c = rng.choice(profissoes)
    credencial = f"'{crm()}'" if c else 'NULL'
    nome_social = f"'{fake.name()}'" if rng.randint(1, 6) == 6 else 'NULL'
    print(f"({i}, {credencial}, {nome_social}, '{fake.name()}', '{prof}')", end=';\n' if i == quantidade_profissionais_saude - 1 else ',\n')


etnias = [
    "'Amarelo'",
    "'Indígena'",
    "'Branco'",
    "'Preto'",
    "'Pardo'",
    'NULL'
]

genero = [
    "'Homem'",
    "'Mulher'",
    "'Não binário'",
    "'Outro'",
    'NULL'
]

tipos_sanguineos = [
    'O', 'A', 'B', 'AB'
]

fatores_rh = '+-'

religioes = [
    'Católica',
    'Protestante',
    'Ortodoxa',
    'Batista',
    'Testemunha de Jeová',
    'Hindu',
    'Sunita',
    'Xiita'
]

print('INSERT INTO Paciente')
print('(CodPaciente, Etnia, Genero, TipoSanquineo, DataNasc, Religiao, CPF, RG, telefone, Endereco, Email, NomeSocial, NomeCivil)')
print('VALUES')
quantidade_pacientes = 100
out = []
for i in range(quantidade_pacientes):
    nome_social = f"'{fake.name()}'" if rng.randint(1, 6) == 6 else 'NULL'
    out.append(f"({i}, {rng.choice(etnias)}, {rng.choice(genero)}, '{rng.choice(tipos_sanguineos) + rng.choice(fatores_rh)}', '{fake.past_datetime().isoformat()}', '{rng.choice(religioes)}', '{str(rng.randint(1, 99999999999)).zfill(11)}', '{str(rng.randint(1, 999999999)).zfill(9)}', '{fake.phone_number()}', '{fake.address()}', '{fake.email()}', {nome_social}, '{fake.name()}')")
print(',\n'.join(out), end=';\n')

print('INSERT INTO Parente')
print('(CodParente, CodPai, CodFilho)')
print('VALUES')
quantidade_parentescos = 20
out = []
for i in range(quantidade_parentescos):
    pai = rng.randrange(quantidade_pacientes)
    filho = rng.randrange(quantidade_pacientes)
    while filho == pai:
        rng.randrange(quantidade_pacientes)
    out.append(f'({i}, {pai}, {filho})')
print(',\n'.join(out), end=';\n')

print(f'''
    INSERT INTO Cirurgia
    (CodCirurgia, CodPaciente, Descricao, Data_, Duracao, Complicacoes, TempoRecuperacao)
    VALUES
    (0, {rng.randrange(quantidade_pacientes)}, 'Exérese de calázio', '{fake.past_datetime().isoformat()}', 10, NULL, 3),
    (1, {rng.randrange(quantidade_pacientes)}, 'Extração do siso', '{fake.past_datetime().isoformat()}', 40, NULL, 13),
    (2, {rng.randrange(quantidade_pacientes)}, 'Radiocirurgia estereotáxica para cavernoma', '{fake.past_datetime().isoformat()}', 40, NULL, 9),
    (3, {rng.randrange(quantidade_pacientes)}, 'Angioplastia coronária para infarto', '{fake.past_datetime().isoformat()}', 70, 'Reestenose coronariana', 16),
''')



