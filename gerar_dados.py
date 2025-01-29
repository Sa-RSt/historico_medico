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
N = 30
for i in range(N):
    prof, c = rng.choice(profissoes)
    credencial = f"'{crm()}'" if c else 'NULL'
    nome_social = f"'{fake.name()}'" if rng.randint(1, 6) == 6 else 'NULL'
    print(f"({i}, {credencial}, {nome_social}, '{fake.name()}', '{prof}')", end=';\n' if i == N - 1 else ',\n')
