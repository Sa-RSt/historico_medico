from faker import Faker
from random import Random
import itertools

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


alergias = [
    'Amendoim',
    'Ovoalbumina',
    'Caseína',
    'Crustáceos',
    'Moluscos',
    'Glúten',
    'Antibióticos beta-lactâmicos',
    'Insulina',
    'Carbamazepina',
    'Anti-inflamatórios não esteroidais'
]


print('INSERT INTO Alergia')
print('(CodAlergia, Alergenico)')
print('VALUES')
print(',\n'.join(f'({i}, {repr(x)})' for i, x in enumerate(alergias)) + ';')


print('INSERT INTO AlergiaPaciente')
print('(CodAlergiaPaciente, CodAlergia, CodPaciente)')
print('VALUES')
print(',\n'.join(f'({i}, {rng.randrange(0, len(alergias))}, {rng.randrange(0, quantidade_pacientes)})' for i in range(9)) + ';')


especialidades = [
    'Neurologia',
    'Cirurgia geral',
    'Cirurgia cardiotorácica',
    'Neurocirurgia',
    'Cirurgia gastrointestinal',
    'Radiologia',
    'Pediatria',
    'Psiquiatria',
    'Cardiologia',
    'Hematologia',
    'Hepatologia',
    'Ortopedia',
    'Otorrinolaringologia'
]

print('INSERT INTO Especialidade')
print('(CodEsp, CodProfissional, Desc_)')
print('VALUES')
print(',\n'.join(f'({i}, {rng.randrange(0, quantidade_profissionais_saude)}, {rng.choice(especialidades)})' for i in range(quantidade_profissionais_saude*3//2)) + ';')


print('INSERT INTO ProfissionalParticipanteCirurgia')
print('(CodPPC, CodCirurgia, CodPaciente, CodProfissional)')
print('VALUES')
print(',\n'.join(f'({i}, {rng.randrange(0, 4)}, {rng.randrange(0, quantidade_pacientes)}, {rng.randrange(0, quantidade_profissionais_saude)})' for i in range(6) )+ ';')


print('INSERT INTO Consulta')
print('(CodConsulta, CodProfissional, CodPaciente, DataHora, Motivo)')
print('VALUES')
print(',\n'.join(f'({i}, {rng.randrange(0, quantidade_profissionais_saude)}, {rng.randrange(0, quantidade_pacientes)}, {repr(fake.past_datetime().isoformat())}, {repr(fake.text())})' for i in range(2*quantidade_pacientes)) + ';')


def cid():
    c = '123456789'
    c1 = c + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join([rng.choice(c1), rng.choice(c1), rng.choice(c), rng.choice(c1)])


print('INSERT INTO Diagnostico')
print('(CodDiagnostico, CodConsulta, CID)')
print('VALUES')
print(',\n'.join(f'({i}, {rng.randrange(0, 2*quantidade_pacientes)}, {repr(cid())}, {repr(fake.past_datetime().isoformat())})' for i in range(2*quantidade_pacientes) )+ ';')


marcas_vacina = [
    'Seqirus',
    'Pfizer',
    'AstraZeneca',
    'GSK',
    'BioNTech'
]

nomes_vacina = ['DTP: difteria, tétano e coqueluche                                                                                                                                                                          [0/134]',
 'HiB: Haemophilus influenzae tipo b  ',
 'VIP: poliomielite inativada  ',
 'VOP: poliomielite oral  ',
 'MMR: sarampo, caxumba e rubéola  ',
 'Varicela: vírus vivo atenuado  ',
 'HPV: papilomavírus humano  ',
 'Influenza: vírus inativado  ',
 'Pneumocócica Conjugada: proteção contra pneumococo  ',
 'Meningocócica Conjugada: proteção contra meningococo   ',
 'Hepatite A e B: combinada  ',
 'HibMenCY: Hib e meningococo C e Y  ',
 'RVA: rotavírus atenuado  ',
 'Febre Amarela: vírus vivo atenuado  ',
 'Tifoide: polissacarídica  ',
 'Cólera: oral inativada  ',
 'Zoster: herpes zoster  ',
 'Covid-19: mRNA, vetor viral  ',
 'HibMenCY-TT: Hib, meningococo C e Y  ',
 'Acelular pertussis (aP): componente celular  ',
 'DTaP: difteria, tétano e coqueluche acelular  ',
 'Td: tétano e difteria  ',
 'HPV-9: nove tipos de HPV  ',
 'Hepatite E: recombinante  ',
 'Dengue: vírus atenuado  ',
 'Bacillus Calmette-Guérin: contra tuberculose  ',
 'Rage: vírus inativado  ',
 'Anthrax: bactéria inativada  ',
 'Varíola: vírus vivo atenuado  ',
 'Encefalite Japonesa: vírus inativado  ',
 'Raiva: vírus inativado  ',
 'Fiebre Tifoidea: oral atenuada  ',
 'Fiebre Hemorrágica: vírus inativado  ',
 'Meningocócica B: recombinante  ',
 'Gripe: quadrivalente inativada  ',
 'Sarampo: apenas sarampo  ',
 'Difteria: toxoide  ',
 'Tétano: toxoide  ',
 'Poliomielite: vivo oral  ',
 'Varicela Zoster: viva atenuada  ',
 'Parotidite: vírus vivo  ',
 'Rubéola: vírus vivo  ',
 'Meningocócica C: conjugada  ',
 'Encefalite da Carrapato: vírus inativado  ',
 'Rabia: vírus inativado  ',
 'Tétano Diftérico: combinado  ',
 'Tifóide: polissacarídeo Vi']


quantidade_vacinas = 20

print('INSERT INTO Vacina')
print('(CodVacina, CID, Marca, Nome)')
print('VALUES')
print(',\n'.join(f'({i}, {repr(cid())}, {repr(rng.choice(marcas_vacina))}, {repr(rng.choice(nomes_vacina))}, {repr(fake.past_datetime().isoformat())})' for i in range(quantidade_vacinas) )+ ';')


print('INSERT INTO Vacinou')
print('(CodVacinou, CodPaciente, CodVacina, Data)')
print('VALUES')
print(',\n'.join(f'({i}, {rng.randrange(0, quantidade_pacientes)}, {rng.randrange(0, quantidade_vacinas)}, {repr(fake.past_date().isoformat())})' for i in range(quantidade_pacientes*3) )+ ';')


principios_ativos = [
    'Paracetamol',
    'Ibuprofeno',
    'Dipirona sódica',
    'Dipirona mono-hidratada',
    'Amoxicilina',
    'Captopril',
    'Metformina',
    'Atorvastatina',
    'Omeprazol',
    'Cetirizina',
    'Salbutamol',
    'Losartana',
    'Atenolol',
    'Hidroclorotiazida',
    'Levotiroxina',
    'Ranitidina',
    'Simvastatina',
    'Furosemida',
    'Azitromicina',
    'Clonazepam',
    'Diazepam',
    'Ciproterona',
    'Fluticasona',
    'Cefalexina',
    'Bupropiona',
    'Loratadina',
    'Ácido fusídico'
]

nomes_comerciais = [['Tylenol',
  'Panadol',
  'Dôrico',
  'Vick Pyrena',
  'Sonridor',
  'Febrasil',
  'Paradoro',
  'Alivium',
  'Multisoro',
  'Paracetamol EMS'],
 ['Advil',
  'Alivium',
  'Buprovil',
  'Dalsy',
  'Doralflex',
  'Ibupril',
  'Ibuprofan',
  'Maxofen',
  'Motrin',
  'Nurofen',
  'Profen',
  'Spidufen',
  'Tabalon',
  'Vantil'],
 ['Novalgina',
  'Neosaldina',
  'Dorflex',
  'Anador',
  'Magnopyrol',
  'Doraliv',
  'Lisador',
  'Maxalgina',
  'Piralgina',
  'Nóvex',
  'Dipimed',
  'D-500'],
 ['Novalgina',
  'Neo Química Dipirona',
  'Dausmed',
  'Baralgin',
  'Analgex',
  'Magnopirol',
  'Dipimed',
  'Dipironax',
  'Dorico',
  'Antalfebrin',
  'Maxiliv',
  'Doralgin',
  'Pirona',
  'Dipirona Teuto',
  'Rehapirin'],
 ['Amoxil',
  'Amoxilin',
  'Novamox',
  'Trimox',
  'Moxatag',
  'Amoxil BD',
  'Amoxibiotic',
  'Amoxicaps',
  'Amoximed',
  'Amoxan',
  'Gramox',
  'Velamox'],
 ['Capoten',
  'Capotena',
  'Capozide',
  'Captotec',
  'Inibace',
  'Capoten D',
  'Hypotril'],
 ['Glifage',
  'Glifage XR',
  'Dimefor',
  'Glucoformin',
  'Diaformin',
  'Metofage',
  'Glicon',
  'Glifor',
  'Metformin',
  'Glyciphage',
  'Riomet'],
 ['Lipitor',
  'Sortis',
  'Tahor',
  'Atorvast',
  'Citalor',
  'Lipilan',
  'Torvacard',
  'Atorvox',
  'Atocor',
  'Ridalip'],
 ['Losec',
  'Prilosec',
  'Zegerid',
  'Omeprazol Medley',
  'Omeprazol Teuto',
  'Omeprazol EMS',
  'Omeprazol Sandoz',
  'Omeprazol Germed',
  'Omeprazol Biolab',
  'Omeprazol Eurofarma',
  'Omeprazol Aché',
  'Omeprazol Neo Química',
  'Omeprazol Legrand',
  'Omeprazol Mylan',
  'Omeprazol Biosintética',
  'Omeprazol Cimed'],
 ['Zyrtec',
  'Zyrtec-D',
  'Reactine',
  'Triz',
  'Cetirizina Sandoz',
  'Cetirizina Actavis',
  'Cetirizina Teva',
  'Hidrozine',
  'Aller-Tec',
  'Cetirinax',
  'Cetirizina EMS',
  'Cetirizina Medley'],
 ['Aerolin', 'Ventolin', 'Sultolin', 'Butovent', 'Stertak'],
 ['Cozaar',
  'Aradois',
  'Losartan',
  'Zart',
  'Losartana Plus',
  'Losacor',
  'Vasartan',
  'Hipertens',
  'Losart',
  'Losazid',
  'Ratiostar'],
 ['Tenormin', 'Atenol', 'Blokium', 'Atenolan', 'Atenolol Kabi'],
 ['Esidrix',
  'HydroDIURIL',
  'Microzide',
  'Oretic',
  'Neo Lotan H',
  'Drenol',
  'Diurix'],
 ['Euthyrox',
  'Synthroid',
  'Levoxyl',
  'Thyrax',
  'Eltroxin',
  'Tirosint',
  'Levothroid',
  'Unithroid'],
 ['Zantac', 'Ulceranin', 'Sovran', 'Antak', 'Azantac', 'Ranitil', 'Ranid'],
 ['Zocor',
  'Sinvastatil',
  'Sinvaxs',
  'Sinvax',
  'Lipovas',
  'Vaslip',
  'Sinvasterol',
  'Sinvastamed',
  'Sinvatin'],
 ['Lasix',
  'Fursemide',
  'Furosemida Neuro',
  'Furosemida EMS',
  'Frusid',
  'Profurosemide',
  'Diuremin'],
 ['Zitromax',
  'Azitromed',
  'Astro',
  'Azitrocin',
  'Azitrin',
  'Aziwell',
  'Azitro',
  'Azitromicina EMS',
  'Zitroneo',
  'Azi',
  'Azimix'],
 ['Rivotril', 'Klonopin', 'Paxam', 'Clonotril', 'Clonotrilid', 'Clonex'],
 ['Valium',
  'Diazepac',
  'Diazepan',
  'Ansiopax',
  'Diazepax',
  'Diazera',
  'Pacif',
  'Observação: Esta lista pode variar conforme a localização e as regulamentações de saúde locais. Para informações precisas e atualizadas, consulte fontes oficiais ou farmacêuticas.'],
 ['Androcur', 'Diane 35', 'Cyprostat', 'Cyproplex', 'Proviron'],
 ['Flixonase',
  'Flonase',
  'Flixonase Nasule',
  'Avamys',
  'Flixotide',
  'Flixonase Spray',
  'Nasonex (associado com outras substâncias)',
  'Seretide (associado com Salmeterol)'],
 ['Keflex', 'Ceporex', 'Dermaciclina', 'Cefalexina EMS', 'Alektos'],
 ['Bup', 'Wellbutrin', 'Zyban', 'Buprovil', 'Buprex', 'Quilion'],
 ['Claritin',
  'Claritin D',
  'Lorfast',
  'Loratamed',
  'Lorax',
  'Claritin Reditabs',
  'Claritine',
  'Alavert',
  'Loratyne',
  'Sempre Livre Loratadina']]


print('INSERT INTO Remedio')
print('(CodRemedio, PrincipioAtivo)')
print('VALUES')
print(',\n'.join(f'({i}, {repr(pa)})' for i, pa in enumerate(principios_ativos)) + ';')


print('INSERT INTO NomeComercialRemedio')
print('(CodNomeCom, CodRemedio, NomeComercial)')
print('VALUES')
for i, nc in enumerate(nomes_comerciais):
    if i == len(nc) - 1:
        end = ';'
    else:
        end = ',\n'
    print(',\n'.join(f'({j}, {i}, {repr(nome)})' for j, nome in enumerate(nc)), end=end)


def produto_cartesiano(*listas):
    if len(listas) == 1:
        return listas[0]
    acc = listas[0]
    for L in listas[1:]:
        tmp = []
        for left in acc:
            for right in L:
                tmp.append(left + right)
        acc = tmp
    return acc


dosagens = produto_cartesiano(
    ['1/4 cp', '1/2 cp', '1 cp', '2 cp', '3 cp', '4 cp', '6 cp', '1 gota', '5 gotas', '10 gotas', '30 gotas', '12 gotas'],
    ['', ' sublingual'],
    [' todos os dias', ' em dias alternados', ' semanalmente', ' a cada três dias'],
    [' após as refeições', ' antes de dormir', ' depois do almoço', ' de 6 em 6h', 'de 8 em 8h']
)


print('INSERT INTO Medicacao')
print('(CodMedicacao, CodRemedio, CodPaciente_Automedicacao, CodConsulta, Data_, Dose)')
print('VALUES')
out = []
for id in range(50):
    am = rng.random() < .5
    if am:
        out.append(f'({id}, {rng.randrange(len(principios_ativos))}, {rng.randrange(quantidade_pacientes)}, NULL, {repr(fake.past_date().isoformat())}, {repr(rng.choice(dosagens))})')

vars_exames_quant = [('Hemoglobina', '13.8-17.2 g/dL (homens), 12.1-15.1 g/dL (mulheres)'),
 ('Hematócrito', '40.7-50.3% (homens), 36.1-44.3% (mulheres)'),
 ('Leucócitos (WBC)', '4,500-11,000 células/µL'),
 ('Plaquetas', '150,000-450,000/µL'),
 ('Glicose', '70-99 mg/dL (jejum)'),
 ('Creatinina', '0.7-1.3 mg/dL (homens), 0.6-1.1 mg/dL (mulheres)'),
 ('Ureia', '6-20 mg/dL'),
 ('Colesterol Total', 'menor que 200 mg/dL'),
 ('LDL (Colesterol Ruim)', 'menor que 100 mg/dL'),
 ('HDL (Colesterol Bom)',
  'maior que 40 mg/dL (homens), maior que 50 mg/dL (mulheres)'),
 ('Triglicerídeos', 'menor que 150 mg/dL'),
 ('TSH', '0.4-4.0 mIU/L'),
 ('T4 Livre', '0.8-1.8 ng/dL'),
 ('Ferro', '60-170 µg/dL'),
 ('Transferrina', '200-350 mg/dL'),
 ('Ferritina', '24-336 ng/mL (homens), 11-307 ng/mL (mulheres)'),
 ('Ácido Úrico', '3.4-7.0 mg/dL (homens), 2.4-6.0 mg/dL (mulheres)'),
 ('Bilirrubina Total', '0.1-1.2 mg/dL'),
 ('AST (TGO)', '10-40 U/L'),
 ('ALT (TGP)', '7-56 U/L')]


print('INSERT INTO Variavel')
print('(CodVariavel, Nome, ValoresReferencia)')
print('VALUES')
print(',\n'.join((f'({i}, {repr(n)}, {repr(v)})' for i, (n, v) in enumerate(vars_exames_quant))) + ';\n')


metodos_analise = ['Espectrofotometria',
 'Eletroforese',
 'Imunoensaio Enzimático (ELISA)',
 'Cromatografia Líquida de Alta Eficiência (HPLC)',
 'Espectrometria de Massas',
 'Radioimunoensaio',
 'Quimioluminescência',
 'Citometria de Fluxo',
 'Teste de Coagulação (Coagulometria)',
 'Análise de Gases Sanguíneos',
 'Turbidimetria',
 'Potenciometria',
 'Nephelometria',
 'Ensaio de Ligação Competitiva',
 'PCR (Reação em Cadeia da Polimerase)']


orgaos = ['Coração',
 'Pulmões',
 'Fígado',
 'Rins',
 'Cérebro',
 'Estômago',
 'Intestino Delgado',
 'Intestino Grosso',
 'Pâncreas',
 'Baço',
 'Vesícula Biliar',
 'Tireoide',
 'Glândulas Adrenais',
 'Olhos',
 'Ouvidos']

tipos_ex_imagem = ['Ultrassonografia',
 'Ressonância Magnética (RM)',
 'Tomografia Computadorizada (TC)',
 'Radiografia',
 'Mamografia',
 'Tomografia por Emissão de Positrons (PET)',
 'Cintilografia',
 'Eletroencefalograma (EEG)',
 'Eletrocardiograma (ECG)',
 'Densitometria Óssea',
 'Fluoroscopia',
 'Angiografia',
 'Ecocardiograma']


tipos_ex_quant = ['Exame de Sangue']


cond_coop = ['Paciente não realizou o jejum indicado antes do exame de sangue.  ',
 'Paciente manteve os olhos fechados durante todo o processo do EEG.  ',
 'Relatou ter tomado medicação não prescrita antes do exame.  ',
 'Paciente não conseguiu permanecer imóvel durante a ressonância magnética.  ',
 'Instruções para evitar cafeína não foram seguidas, paciente consumiu café pela manhã.  ',
 'Relatou ter ingerido alimentos gordurosos na noite anterior ao teste de colesterol.  ',
 'Não foi realizada a ingestão adequada de água antes do ultrassom abdominal.  ',
 'Paciente cooperou e seguiu todas as orientações para a coleta de urina.  ',
 'Paciente apresentou ansiedade, o que pode ter afetado os resultados do teste de função pulmonar.  ',
 'O consentimento informado foi assinado e todas as informações foram compreendidas pelo paciente.']


arquivos = []
tipos_arquivo = ['PDF', 'PNG', 'JPG', 'RTF']
exames = []
exames_vars = []
arquivoexameimagem = []

for i in range(20):
    am = rng.random() < .3
    if am:
        esp = rng.choice([0, 2])
        
        if esp == 2:
            e = f'({i}, {rng.randrange(quantidade_pacientes)}, NULL, {esp}, {repr(fake.past_datetime().isoformat())}, "Exame de Sangue", {repr(fake.text())}, "OK", NULL, NULL)'
            for j in range(rng.randrange(20)):
                v = rng.randrange(len(vars_exames_quant))
                veq = f'({v}, {i}, {j}, {rng.random() * 100}, {rng.choice(metodos_analise)})'
                exames_vars.append(veq)
        else:
            tipo = rng.choice(tipos_ex_imagem)
            e = f'({i}, {rng.randrange(quantidade_pacientes)}, NULL, {esp}, {repr(fake.past_datetime().isoformat())}, {repr(tipo)}, {repr(fake.text())}, "OK", {repr(rng.choice(orgaos))}, NULL)'
            for m in range(rng.randint(1, 4)):
                arqid = len(arquivos)
                ta = rng.choice(tipos_arquivo)
                arquivos.append(f'({arqid}, {repr("exame-{}-.{}".format(arqid, ta.lower()))}, {repr(ta)}, "teste")')
                arquivoexameimagem.append(f'({arqid}, {i}, {m})')
    else:
        esp = rng.choice([0,1, 2])
        cons = rng.randrange(2*quantidade_pacientes)
        
        if esp == 2:
            e = f'({i}, NULL, {cons}, {esp}, {repr(fake.past_datetime().isoformat())}, "Exame de Sangue", {repr(fake.text())}, {repr(rng.choice(cond_coop))}, NULL, NULL)'
            for j in range(rng.randrange(20)):
                v = rng.randrange(len(vars_exames_quant))
                veq = f'({v}, {i}, {j}, {rng.random() * 100}, {rng.choice(metodos_analise)})'
                exames_vars.append(veq)
        elif esp == 0:
            tipo = rng.choice(tipos_ex_imagem)
            e = f'({i}, NULL, {cons}, {esp}, {repr(fake.past_datetime().isoformat())}, {repr(tipo)}, {repr(fake.text())}, {repr(rng.choice(cond_coop))}, {repr(rng.choice(orgaos))}, NULL)'
            for m in range(rng.randint(1, 4)):
                arqid = len(arquivos)
                ta = rng.choice(tipos_arquivo)
                arquivos.append(f'({arqid}, {repr("exame-{}-.{}".format(arqid, ta.lower()))}, {repr(ta)}, "teste")')
                arquivoexameimagem.append(f'({arqid}, {i}, {m})')
        else:
            tipo = 'Laudo'
            arqid = len(arquivos)
            ta = rng.choice(['PDF', 'RTF'])
            arquivos.append(f'({arqid}, {repr("laudo-{}-.{}".format(arqid, ta.lower()))}, {repr(ta)}, "teste")')
            e = f'({i}, NULL, {cons}, {esp}, {repr(fake.past_datetime().isoformat())}, {repr(tipo)}, {repr(fake.text())}, "OK", NULL, {arqid})'
    exames.append(e)


print('INSERT INTO Exame')
print('(CodExame, CodPaciente, CodConsulta_Prescricao, TipoEspecializacao, DataHora, Motivo, Tipo, CondicoesCooperacao, Orgaos, CodArquivo_Laudo)')
print('VALUES')
print(',\n'.join(exames) + ';\n')

print('INSERT INTO Arquivo')
print('(CodArquivo, Nome, Tipo, Conteudo)')
print('VALUES')
print(',\n'.join(arquivos) + ';\n')

print('INSERT INTO ArquivoExameImagem')
print('(CodArquivo, CodExame, CodAEI)')
print('VALUES')
print(',\n'.join(arquivoexameimagem) + ';\n')

def stringAleatoria(n):
    from string import ascii_letters, digits
    pool = ascii_letters + digits
    return ''.join(rng.choices(pool, k=n))


tipos_dispo = ['Smartphone',
 'Laptop',
 'Tablet',
 'Desktop',
 'Celular',
 'Monitor de Saúde Vestível',
 'Notebook Médico',
 'Tablets para Ambulâncias',
 'Equipamento Médico Conectado']


print('INSERT INTO Dispositivo')
print('(CodDispositivo, ChaveSeguranca, Tipo)')
print('VALUES')
print(',\n'.join((f'({i}, {repr(stringAleatoria(32))}, {repr(rng.choice(tipos_dispo))})' for i in range(13))) + ';\n')


niveis_aut = [
    'Read',
    'Append',
    'Write'
]

print('INSERT INTO AcessoBD')
print('(CodAcesso, CodProfissional, CodDispositivo, NivelAutorizacao, NomeUsuario, Senha)')
print('VALUES')
print(',\n'.join((f'({i}, {rng.randrange(quantidade_profissionais_saude)}, {rng.randrange(13)}, {repr(rng.choice(niveis_aut))}, {repr(fake.user_name())}, {repr(fake.password())})' for i in range(13)) )+ ';\n')



nomes_tabelas = ['Paciente',
 'Parente',
 'Cirurgia',
 'Alergia',
 'AlergiaPaciente',
 'Especialidade',
 'ProfissionalSaude',
 'ProfissionalParticipanteCirurgia',
 'Consulta',
 'Diagnostico',
 'Vacina',
 'Vacinou',
 'Remedio',
 'NomeComercialRemedio',
 'Medicacao',
 'Exame',
 'Arquivo',
 'ArquivoExameImagem',
 'Variavel',
 'VariavelExameQuantitativo',
 'Dispositivo',
 'AcessoBD',
 'RegistroAcesso']


def rngtabelas():
    return ', '.join(rng.choices(nomes_tabelas, k=rng.randrange(1, 5)))


print('INSERT INTO RegistroAcesso')
print('(CodRegistroAcesso, CodAcesso, CodProfissional, CodDispositivo, CodPaciente, DataHora, CRUouD, Tabelas, CodigoRegistroAfetado)')
print('VALUES')
print(',\n'.join((f'({i}, {rng.randrange(13)}, {rng.randrange(quantidade_profissionais_saude)}, {rng.randrange(13)}, {rng.randrange(quantidade_pacientes)}, {repr(fake.past_datetime().isoformat())}, {repr(rng.choice("CRUD"))}, {repr(rngtabelas())}, {rng.randrange(5)})' for i in range(20))) + ';\n')
