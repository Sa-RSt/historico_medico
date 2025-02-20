CREATE TABLE
    Paciente (CodPaciente INT, Etnia VARCHAR(1024), Genero VARCHAR(1024), TipoSanguineo VARCHAR(1024) NOT NULL, DataNasc TIMESTAMP, Religiao VARCHAR(1024), CPF CHAR(11) NOT NULL, RG VARCHAR(1024) NOT NULL, telefone VARCHAR(1024), Endereco VARCHAR(1024), Email VARCHAR(1024), NomeSocial VARCHAR(1024), NomeCivil VARCHAR(1024) NOT NULL, PRIMARY KEY (CodPaciente));

CREATE TABLE
    Parente (CodParente INT, CodPai INT, CodFilho INT, PRIMARY KEY (CodParente, CodFilho, CodPai), FOREIGN KEY (CodFilho) REFERENCES Paciente (CodPaciente), FOREIGN KEY (CodPai) REFERENCES Paciente (CodPaciente));

CREATE TABLE
    Cirurgia (CodCirurgia INT, CodPaciente INT, Descricao TEXT, Data_ TIMESTAMP, Duracao INT, Complicacoes TEXT, TempoRecuperacao INT, PRIMARY KEY (CodCirurgia, CodPaciente), FOREIGN KEY (CodPaciente) REFERENCES Paciente (CodPaciente));

CREATE TABLE
    Alergia (CodAlergia INT, Alergenico VARCHAR(1024), PRIMARY KEY (CodAlergia));

CREATE TABLE
    AlergiaPaciente (CodAlergiaPaciente INT, CodAlergia INT, CodPaciente INT, Desc_ VARCHAR(1024), PRIMARY KEY (CodAlergiaPaciente, CodAlergia, CodPaciente), FOREIGN KEY (CodAlergia) REFERENCES Alergia (CodAlergia), FOREIGN KEY (CodPaciente) REFERENCES Paciente (CodPaciente));

CREATE TABLE
    ProfissionalSaude (CodProfissional INT, CRM CHAR(13), NomeSocial VARCHAR(1024), NomeCivil VARCHAR(1024) NOT NULL, Profissao VARCHAR(1024) NOT NULL, PRIMARY KEY (CodProfissional));

CREATE TABLE
    Especialidade (CodEsp INT, CodProfissional INT, Desc_ VARCHAR(1024), PRIMARY KEY (CodEsp, CodProfissional), FOREIGN KEY (CodProfissional) REFERENCES ProfissionalSaude (CodProfissional));

CREATE TABLE
    ProfissionalParticipanteCirurgia (CodPPC INT, CodCirurgia INT, CodPaciente INT, CodProfissional INT, PRIMARY KEY (CodPPC, CodCirurgia, CodPaciente, CodProfissional), FOREIGN KEY (CodCirurgia) REFERENCES Cirurgia (CodCirurgia), FOREIGN KEY (CodPaciente) REFERENCES Paciente (CodPaciente), FOREIGN KEY (CodProfissional) REFERENCES ProfissionalSaude (CodProfissional));

CREATE TABLE
    Consulta (CodConsulta INT, CodProfissional INT, CodPaciente INT, DataHora TIMESTAMP, Motivo VARCHAR(1024), PRIMARY KEY (CodConsulta, CodProfissional, CodPaciente), FOREIGN KEY (CodProfissional) REFERENCES ProfissionalSaude (CodProfissional), FOREIGN KEY (CodPaciente) REFERENCES Paciente (CodPaciente));

CREATE TABLE
    Diagnostico (CodDiagnostico INT, CodConsulta INT, CID VARCHAR(1024), PRIMARY KEY (CodDiagnostico, CodConsulta), FOREIGN KEY (CodConsulta) REFERENCES Consulta (CodConsulta));

CREATE TABLE
    Vacina (CodVacina INT, CID VARCHAR(1024), Marca VARCHAR(1024), Nome VARCHAR(1024), PRIMARY KEY (CodVacina));

CREATE TABLE
    Vacinou (CodVacinou INT, CodPaciente INT, CodVacina INT, DATA DATE, PRIMARY KEY (CodVacinou, CodPaciente, CodVacina), FOREIGN KEY (CodPaciente) REFERENCES Paciente (CodPaciente), FOREIGN KEY (CodVacina) REFERENCES Vacina (CodVacina));

CREATE TABLE
    Remedio (CodRemedio INT, PrincipioAtivo VARCHAR(1024), PRIMARY KEY (CodRemedio));

CREATE TABLE
    NomeComercialRemedio (CodNomeCom INT, CodRemedio INT, NomeComercial VARCHAR(1024), PRIMARY KEY (CodNomeCom, CodRemedio), FOREIGN KEY (CodRemedio) REFERENCES Remedio (CodRemedio));

CREATE TABLE
    Medicacao (CodMedicacao INT, CodRemedio INT, CodPaciente_Automedicacao INT, CodConsulta INT, CodPaciente INT, Data_ DATE, Dose VARCHAR(1024), PRIMARY KEY (CodMedicacao, CodRemedio), FOREIGN KEY (CodRemedio) REFERENCES Remedio (CodRemedio), FOREIGN KEY (CodPaciente_Automedicacao) REFERENCES Paciente (CodPaciente), FOREIGN KEY (CodConsulta) REFERENCES Consulta (CodConsulta), FOREIGN KEY (CodPaciente) REFERENCES Paciente (CodPaciente));

CREATE TABLE
    Arquivo (CodArquivo INT, Nome VARCHAR(1024), Tipo VARCHAR(1024), Conteudo VARCHAR(1024), PRIMARY KEY (CodArquivo));

CREATE TABLE
    Exame (CodExame INT, CodPaciente INT, CodConsulta_Prescricao INT, TipoEspecializacao INT, DataHora TIMESTAMP, Motivo VARCHAR(1024), Tipo VARCHAR(1024), CondicoesCooperacao VARCHAR(1024), Orgaos VARCHAR(1024), CodArquivo_Laudo INT, PRIMARY KEY (CodExame, CodPaciente), FOREIGN KEY (CodPaciente) REFERENCES Paciente (CodPaciente), FOREIGN KEY (CodConsulta_Prescricao) REFERENCES Consulta (CodConsulta), FOREIGN KEY (CodArquivo_Laudo) REFERENCES Arquivo (CodArquivo));

CREATE TABLE
    ArquivoExameImagem (CodArquivo INT, CodExame INT, CodAEI INT, PRIMARY KEY (CodArquivo, CodExame, CodAEI), FOREIGN KEY (CodArquivo) REFERENCES Arquivo (CodArquivo), FOREIGN KEY (CodExame) REFERENCES Exame (CodExame));

CREATE TABLE
    Variavel (CodVariavel INT, Nome VARCHAR(1024), ValoresReferencia VARCHAR(1024), PRIMARY KEY (CodVariavel));

CREATE TABLE
    VariavelExameQuantitativo (CodVariavel INT, CodExame INT, CodVEQ FLOAT, Valor FLOAT, MetodoAnalise VARCHAR(1024), PRIMARY KEY (CodVariavel, CodExame, CodVEQ), FOREIGN KEY (CodVariavel) REFERENCES Variavel (CodVariavel), FOREIGN KEY (CodExame) REFERENCES Exame (CodExame));

CREATE TABLE
    Dispositivo (CodDispositivo INT, ChaveSeguranca VARCHAR(1024), Tipo VARCHAR(1024), PRIMARY KEY (CodDispositivo));

CREATE TABLE
    AcessoBD (CodAcesso INT, CodProfissional INT, CodDispositivo INT, NivelAutorizacao VARCHAR(1024) NOT NULL, NomeUsuario VARCHAR(1024) NOT NULL, Senha VARCHAR(1024) NOT NULL, PRIMARY KEY (CodAcesso, CodProfissional, CodDispositivo), FOREIGN KEY (CodProfissional) REFERENCES ProfissionalSaude (CodProfissional), FOREIGN KEY (CodDispositivo) REFERENCES Dispositivo (CodDispositivo));

CREATE TABLE
    RegistroAcesso (CodRegistroAcesso INT, CodAcesso INT, CodProfissional INT, CodDispositivo INT, CodPaciente INT, DataHora TIMESTAMP, CRUouD CHAR(1), Tabelas VARCHAR(1024), CodigoRegistroAfetado VARCHAR(1024), PRIMARY KEY (CodRegistroAcesso, CodAcesso, CodProfissional, CodDispositivo), FOREIGN KEY (CodAcesso) REFERENCES AcessoBD (CodAcesso), FOREIGN KEY (CodProfissional) REFERENCES ProfissionalSaude (CodProfissional), FOREIGN KEY (CodDispositivo) REFERENCES Dispositivo (CodDispositivo), FOREIGN KEY (CodPaciente) REFERENCES Paciente (CodPaciente));