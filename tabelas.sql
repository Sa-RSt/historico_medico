CREATE TABLE
    ProfissionalSaude (
        CodProfissional INT,
        CRM CHAR(13),
        NomeSocial VARCHAR(64),
        NomeCivil VARCHAR(64) NOT NULL,
        Profissao VARCHAR(64) NOT NULL,
        PRIMARY KEY (CodProfissional)
    );

CREATE TABLE
    Paciente (
        CodPaciente INT,
        Etnia VARCHAR(7),
        Genero VARCHAR(1024),
        TipoSanquineo VARCHAR(10) NOT NULL,
        DataNasc TIMESTAMP,
        Religiao VARCHAR(15),
        CPF CHAR(11) NOT NULL,
        RG VARCHAR(10) NOT NULL,
        telefone VARCHAR(30),
        Endereco VARCHAR(70),
        Email VARCHAR(40),
        NomeSocial VARCHAR(64),
        NomeCivil VARCHAR(64) NOT NULL,
        PRIMARY KEY (CodPaciente)
    );
z