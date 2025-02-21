SET @@session.foreign_key_checks=0;
DELETE FROM RegistroAcesso;
DELETE FROM AcessoBD;
DELETE FROM Dispositivo;
DELETE FROM VariavelExameQuantitativo;
DELETE FROM Variavel;
DELETE FROM ArquivoExameImagem;
DELETE FROM Arquivo;
DELETE FROM Exame;
DELETE FROM Medicacao;
DELETE FROM NomeComercialRemedio;
DELETE FROM Remedio;
DELETE FROM Vacinou;
DELETE FROM Vacina;
DELETE FROM Diagnostico;
DELETE FROM Consulta;
DELETE FROM ProfissionalParticipanteCirurgia;
DELETE FROM ProfissionalSaude;
DELETE FROM Especialidade;
DELETE FROM AlergiaPaciente;
DELETE FROM Alergia;
DELETE FROM Cirurgia;
DELETE FROM Parente;
DELETE FROM Paciente;
SET @@session.foreign_key_checks=1;
INSERT INTO ProfissionalSaude
(CodProfissional, CRM, NomeSocial, NomeCivil, Profissao)
VALUES
(0, 'CRM/MG 794772', NULL, 'Mariah Aparecida', 'Veterinário'),
(1, 'CRM/GO 536110', NULL, 'Thomas Mendonça', 'Médico'),
(2, NULL, NULL, 'Liz Mendes', 'Nutricionista'),
(3, 'CRM/MS 611720', NULL, 'Thiago Carvalho', 'Terapeuta Ocupacional'),
(4, 'CRM/BA 295528', NULL, 'Davi Miguel Sá', 'Fonoaudiólogo'),
(5, NULL, NULL, 'José Nascimento', 'Educador Físico'),
(6, NULL, NULL, 'Clara das Neves', 'Biomédico'),
(7, 'CRM/PI 739426', NULL, 'Brayan Rodrigues', 'Ortopedista'),
(8, 'CRM/BA 325213', NULL, 'Carlos Eduardo Fogaça', 'Ortopedista'),
(9, NULL, NULL, 'Luara Pimenta', 'Assistente Social');
INSERT INTO Paciente
(CodPaciente, Etnia, Genero, TipoSanguineo, DataNasc, Religiao, CPF, RG, telefone, Endereco, Email, NomeSocial, NomeCivil)
VALUES
(0, 'Branco', 'Outro', 'O-', '2025-01-29T18:21:02.808044', 'Sunita', '82962433110', '687649392', '81 0160-9753', 'Estrada Nunes, 33
Vista Do Sol
11587-148 Santos do Campo / PI', 'gabriellynovaes@mail.com', 'Gabrielly Novaes', 'Melina Moreira'),
(1, 'Pardo', 'Não binário', 'O+', '2025-01-30T13:54:34.341176', 'Protestante', '96202214578', '885670548', '+55 31 9659 3423', 'Viaduto de da Luz
Primeiro De Maio
12201868 Moreira de Goiás / DF', 'yanpastor@protonmail.com', NULL, 'Yan Pastor'),
(2, 'Branco', 'Mulher', 'B+', '2025-01-30T04:56:53.159977', 'Batista', '81247977808', '238052748', '11 5159-1795', 'Ladeira Camargo, 35
Lorena
01230-989 Alves / AM', 'mariah.pacheco@tutanota.com', NULL, 'Mariah Pacheco'),
(3, 'Preto', 'Homem', 'O-', '2025-02-15T20:27:29.422023', 'Xiita', '39123105554', '591918702', '+55 71 6151 0903', 'Recanto Costela, 1
São Marcos
91413-145 Cirino do Norte / PE', 'esther.pereira@zoho.com', NULL, 'Esther Pereira'),
(4, 'Indígena', NULL, 'B-', '2025-01-24T23:27:34.756241', 'Protestante', '44602810790', '618100573', '61 3457 9230', 'Loteamento Moura, 81
Vila Esplanada
07698456 Cassiano da Prata / RR', 'ana.cecilia.peixoto@gmail.com', NULL, 'Ana Cecília Peixoto'),
(5, NULL, 'Não binário', 'AB+', '2025-01-24T07:43:46.182632', 'Protestante', '76576521803', '733900803', '+55 (061) 8423 7594', 'Vale de Cardoso, 76
Palmares
09352337 Santos Verde / PA', 'raul.sousa@aol.com', NULL, 'Raul Sousa'),
(6, 'Indígena', 'Mulher', 'AB-', '2025-02-07T23:22:34.742454', 'Xiita', '92310251974', '688479847', '+55 (061) 2714 2787', 'Largo Ana Lívia Martins
Baleia
38120-665 Cunha / AC', 'murilosampaio@tutanota.com', NULL, 'Murilo Sampaio'),
(7, 'Amarelo', 'Não binário', 'O-', '2025-01-24T21:12:03.916163', 'Hindu', '29399384323', '260957516', '+55 71 9344 2176', 'Praia Igor da Cunha
Chácara Leonina
12400-034 Fonseca Verde / AL', 'vitoria.pimenta@fastmail.com', NULL, 'Vitória Pimenta'),
(8, 'Branco', 'Mulher', 'B-', '2025-02-10T06:34:46.188639', 'Católica', '33061243655', '048569709', '(051) 6582-3694', 'Ladeira Farias, 25
Mala E Cuia
04229456 da Rocha / AM', 'sabrinasilva@lycos.com', NULL, 'Sabrina Silva'),
(9, 'Pardo', 'Homem', 'O+', '2025-01-31T04:28:11.035741', 'Batista', '15358600992', '420057910', '41 1465-4611', 'Loteamento Josué Mendes, 8
Novo Glória
45229611 Costa / SC', 'isabella.aragao@outlook.com', NULL, 'Isabella Aragão');
INSERT INTO Parente
(CodParente, CodPai, CodFilho)
VALUES
(0, 0, 9),
(1, 0, 3),
(2, 2, 1),
(3, 7, 3),
(4, 8, 6);

    INSERT INTO Cirurgia
    (CodCirurgia, CodPaciente, Descricao, Data_, Duracao, Complicacoes, TempoRecuperacao)
    VALUES
    (0, 9, 'Exérese de calázio', '2025-01-28T13:57:30.979408', 10, NULL, 3),
    (1, 1, 'Extração do siso', '2025-02-02T11:51:39.061581', 40, NULL, 13),
    (2, 4, 'Radiocirurgia estereotáxica para cavernoma', '2025-01-24T21:24:41.216837', 40, NULL, 9),
    (3, 1, 'Angioplastia coronária para infarto', '2025-02-07T15:27:28.626371', 70, 'Reestenose coronariana', 16);

INSERT INTO Alergia
(CodAlergia, Alergenico)
VALUES
(0, 'Amendoim'),
(1, 'Ovoalbumina'),
(2, 'Caseína'),
(3, 'Crustáceos'),
(4, 'Moluscos'),
(5, 'Glúten'),
(6, 'Antibióticos beta-lactâmicos'),
(7, 'Insulina'),
(8, 'Carbamazepina'),
(9, 'Anti-inflamatórios não esteroidais');
INSERT INTO AlergiaPaciente
(CodAlergiaPaciente, CodAlergia, CodPaciente)
VALUES
(0, 3, 1),
(1, 4, 5),
(2, 6, 2),
(3, 0, 8),
(4, 7, 0),
(5, 9, 1),
(6, 6, 3),
(7, 4, 5),
(8, 7, 9);
INSERT INTO Especialidade
(CodEsp, CodProfissional, Desc_)
VALUES
(0, 2, 'Ortopedia'),
(1, 3, 'Otorrinolaringologia'),
(2, 0, 'Otorrinolaringologia'),
(3, 2, 'Cirurgia cardiotorácica'),
(4, 5, 'Cardiologia'),
(5, 4, 'Cirurgia geral'),
(6, 9, 'Psiquiatria'),
(7, 2, 'Neurologia'),
(8, 7, 'Hepatologia'),
(9, 6, 'Hematologia'),
(10, 8, 'Cirurgia gastrointestinal'),
(11, 5, 'Pediatria'),
(12, 4, 'Cirurgia cardiotorácica'),
(13, 8, 'Ortopedia'),
(14, 0, 'Psiquiatria');
INSERT INTO ProfissionalParticipanteCirurgia
(CodPPC, CodCirurgia, CodPaciente, CodProfissional)
VALUES
(0, 0, 5, 0),
(1, 2, 2, 3),
(2, 3, 5, 9),
(3, 2, 5, 9),
(4, 1, 4, 6),
(5, 3, 1, 0);
INSERT INTO Consulta
(CodConsulta, CodProfissional, CodPaciente, DataHora, Motivo)
VALUES
(0, 9, 3, '2025-01-30T15:28:02.245899', 'Quaerat dolor assumenda dolore voluptatum nesciunt cumque deleniti. Aperiam sint praesentium temporibus. Quibusdam dicta libero ducimus odit voluptatum reiciendis.'),
(1, 5, 2, '2025-01-31T11:56:35.147648', 'Minima soluta nobis. Sapiente nesciunt quaerat rem. Reiciendis maxime totam architecto.\nError quis ipsum. Reiciendis sit itaque fuga.'),
(2, 3, 3, '2025-01-31T00:33:16.485445', 'Ex laudantium ea repudiandae quo. Repellat aperiam odit consectetur enim rerum. Velit laboriosam consequuntur suscipit.'),
(3, 7, 6, '2025-02-14T22:19:18.620664', 'Similique voluptatum alias hic fuga deleniti explicabo. Asperiores aliquid vel laborum tempore velit pariatur nemo.'),
(4, 9, 6, '2025-01-25T02:13:36.793065', 'Impedit culpa veritatis recusandae. Placeat adipisci ullam vitae quam aspernatur.\nFacere adipisci expedita ab. Reprehenderit architecto tempora dignissimos dignissimos.'),
(5, 0, 6, '2025-01-25T20:30:35.613801', 'Ex vero eos soluta mollitia eveniet. Voluptatibus aut neque culpa tempore veniam rem et.\nQuidem enim in aliquid consequatur. Hic praesentium consequatur.'),
(6, 9, 6, '2025-02-05T01:50:07.039141', 'Eius nam porro recusandae. Unde delectus in cupiditate vero excepturi minima.'),
(7, 0, 2, '2025-01-30T01:15:09.955348', 'Ducimus minima neque.\nAut dolorum eligendi quidem tenetur nisi. Architecto ea modi. Minus dolorum ullam cum.'),
(8, 7, 1, '2025-02-01T13:43:04.620653', 'Dolor laborum magnam laudantium vero ipsam. Quia amet numquam ad. Hic voluptatibus sed voluptatem porro aspernatur veniam.'),
(9, 4, 2, '2025-02-10T09:21:35.197371', 'Ipsum quae minima consectetur. Ipsam ratione harum rem. Quas recusandae ipsa dignissimos quae temporibus.\nOdio sit facilis quia perspiciatis.'),
(10, 7, 8, '2025-02-05T05:15:57.714507', 'Aliquam amet expedita enim ab. Ratione perspiciatis voluptas id. Iste excepturi aut sunt recusandae.'),
(11, 7, 8, '2025-02-04T18:39:59.843836', 'Totam impedit laudantium. Blanditiis aspernatur atque quisquam impedit ullam. Nostrum repellendus nam suscipit hic vero.'),
(12, 9, 0, '2025-01-25T12:16:55.654798', 'Quasi dolorum eligendi quasi. Quia maiores similique.\nOfficia blanditiis qui facere perferendis provident. Dolore rerum dolores maxime perferendis.'),
(13, 0, 7, '2025-02-18T09:40:59.896667', 'Quisquam voluptas doloremque consequatur doloremque fugit non. Occaecati tempore autem rerum. Nisi laudantium est vero nam cum soluta.'),
(14, 5, 4, '2025-02-12T22:03:43.699304', 'Ad occaecati ad aliquid dolorem omnis. Reprehenderit exercitationem optio consequatur.\nIpsa facere debitis eveniet voluptates quibusdam fugit. Tempora modi rem voluptatem provident quis.'),
(15, 7, 0, '2025-02-03T18:21:50.062360', 'Nulla itaque corrupti nobis. Excepturi qui fugiat numquam suscipit. At eos corrupti doloremque explicabo quasi illo. Rem velit accusamus minus enim.'),
(16, 6, 3, '2025-02-20T19:09:11.709237', 'Maiores harum rerum dolorum blanditiis voluptatem rem. Nesciunt quam placeat explicabo totam.\nSed reprehenderit nesciunt amet culpa exercitationem. Numquam eum quos nobis voluptates.'),
(17, 8, 1, '2025-02-12T14:21:57.612354', 'Deleniti molestias incidunt veniam cupiditate cumque omnis culpa. Velit odio molestiae harum.'),
(18, 2, 0, '2025-02-18T15:51:44.730744', 'Facere veniam natus illum nostrum rem. Tempore facere voluptatem culpa deserunt. Occaecati libero quasi dolorum tempora earum.'),
(19, 6, 6, '2025-01-22T20:29:35.214736', 'Dicta id ipsa odio perferendis.\nIure rerum consectetur quae eveniet ad labore maxime.\nNatus expedita a deleniti.\nIusto et sapiente veritatis ad hic commodi. Illo consequuntur corporis sint maiores.');
INSERT INTO Diagnostico
(CodDiagnostico, CodConsulta, CID)
VALUES
(0, 10, '1E11'),
(1, 16, '7D2D'),
(2, 9, 'IC2V'),
(3, 12, '625T'),
(4, 3, 'H99N'),
(5, 3, 'AI13'),
(6, 1, 'EH9L'),
(7, 11, '3W8S'),
(8, 11, 'ZC4P'),
(9, 18, 'J13A'),
(10, 8, 'MM66'),
(11, 10, '335B'),
(12, 4, 'JO79'),
(13, 9, '8V44'),
(14, 9, 'CY2K'),
(15, 12, 'MK77'),
(16, 3, 'VV6M'),
(17, 3, 'V88S'),
(18, 1, 'KM3B'),
(19, 18, 'P626');
INSERT INTO Vacina
(CodVacina, CID, Marca, Nome)
VALUES
(0, 'DF1P', 'Seqirus', 'HPV: papilomavírus humano'),
(1, 'QY5T', 'GSK', 'Tétano: toxoide'),
(2, 'ES2O', 'Pfizer', 'Zoster: herpes zoster'),
(3, 'BS4N', 'Seqirus', 'MMR: sarampo, caxumba e rubéola'),
(4, '2Y8D', 'Seqirus', 'Fiebre Tifoidea: oral atenuada'),
(5, 'QH43', 'Pfizer', 'Varicela Zoster: viva atenuada'),
(6, 'A74U', 'GSK', 'Hepatite E: recombinante'),
(7, 'ZA2W', 'Pfizer', 'Difteria: toxoide'),
(8, 'QS9W', 'AstraZeneca', 'Fiebre Tifoidea: oral atenuada'),
(9, 'WD9F', 'Seqirus', 'Td: tétano e difteria');
INSERT INTO Vacinou
(CodVacinou, CodPaciente, CodVacina, Data)
VALUES
(0, 5, 5, '2025-02-10'),
(1, 0, 8, '2025-02-10'),
(2, 2, 4, '2025-02-01'),
(3, 9, 2, '2025-01-26'),
(4, 6, 9, '2025-02-13'),
(5, 4, 7, '2025-02-13'),
(6, 1, 1, '2025-01-23'),
(7, 8, 0, '2025-01-26'),
(8, 1, 3, '2025-01-28'),
(9, 2, 0, '2025-02-13'),
(10, 4, 0, '2025-01-30'),
(11, 7, 5, '2025-02-10'),
(12, 2, 2, '2025-02-12'),
(13, 7, 5, '2025-02-05'),
(14, 8, 6, '2025-02-03'),
(15, 8, 8, '2025-02-16'),
(16, 0, 9, '2025-02-11'),
(17, 1, 8, '2025-02-03'),
(18, 9, 1, '2025-01-25'),
(19, 6, 3, '2025-02-08'),
(20, 4, 8, '2025-01-26'),
(21, 9, 6, '2025-02-04'),
(22, 7, 6, '2025-02-15'),
(23, 9, 9, '2025-01-30'),
(24, 3, 0, '2025-02-17'),
(25, 0, 2, '2025-01-26'),
(26, 4, 8, '2025-02-12'),
(27, 9, 4, '2025-02-07'),
(28, 5, 1, '2025-02-13'),
(29, 7, 4, '2025-02-05');
INSERT INTO Remedio
(CodRemedio, PrincipioAtivo)
VALUES
(0, 'Paracetamol'),
(1, 'Ibuprofeno'),
(2, 'Dipirona sódica'),
(3, 'Dipirona mono-hidratada'),
(4, 'Amoxicilina'),
(5, 'Captopril'),
(6, 'Metformina'),
(7, 'Atorvastatina'),
(8, 'Omeprazol'),
(9, 'Cetirizina'),
(10, 'Salbutamol'),
(11, 'Losartana'),
(12, 'Atenolol'),
(13, 'Hidroclorotiazida'),
(14, 'Levotiroxina'),
(15, 'Ranitidina'),
(16, 'Simvastatina'),
(17, 'Furosemida'),
(18, 'Azitromicina'),
(19, 'Clonazepam'),
(20, 'Diazepam'),
(21, 'Ciproterona'),
(22, 'Fluticasona'),
(23, 'Cefalexina'),
(24, 'Bupropiona'),
(25, 'Loratadina'),
(26, 'Ácido fusídico');
INSERT INTO NomeComercialRemedio
(CodNomeCom, CodRemedio, NomeComercial)
VALUES
(0, 0, 'Alivium'),
(1, 0, 'Vick Pyrena'),
(0, 1, 'Advil'),
(1, 1, 'Motrin'),
(0, 2, 'Dorflex'),
(0, 3, 'Novalgina'),
(1, 3, 'Novalgina'),
(0, 4, 'Amoxilin'),
(1, 4, 'Gramox'),
(0, 5, 'Inibace'),
(0, 6, 'Metformin'),
(0, 7, 'Citalor'),
(1, 7, 'Torvacard'),
(0, 8, 'Omeprazol Germed'),
(1, 8, 'Prilosec'),
(0, 9, 'Zyrtec'),
(0, 10, 'Butovent'),
(0, 11, 'Hipertens'),
(0, 12, 'Tenormin'),
(1, 12, 'Atenolan'),
(0, 13, 'Esidrix'),
(1, 13, 'Esidrix'),
(0, 14, 'Eltroxin'),
(1, 14, 'Unithroid'),
(0, 15, 'Ranid'),
(0, 16, 'Sinvastamed'),
(1, 16, 'Sinvastatil'),
(0, 17, 'Profurosemide'),
(1, 17, 'Diuremin'),
(0, 18, 'Aziwell'),
(0, 19, 'Rivotril'),
(0, 20, 'Ansiopax'),
(1, 20, 'Diazera'),
(0, 21, 'Diane 35'),
(1, 21, 'Cyproplex'),
(0, 22, 'Seretide (associado com Salmeterol)'),
(0, 23, 'Dermaciclina'),
(0, 24, 'Quilion'),
(0, 25, 'Lorfast');INSERT INTO Medicacao
(CodMedicacao, CodRemedio, CodPaciente_Automedicacao, CodConsulta, Data_, Dose)
VALUES
(7, 18, 6, NULL, '2025-02-10', '12 gotas sublingual semanalmente depois do almoço'),
(8, 3, 6, NULL, '2025-02-16', '1/4 cp sublingual semanalmente depois do almoço'),
(9, 24, 2, NULL, '2025-01-24', '10 gotas a cada três dias após as refeições');

INSERT INTO Variavel
(CodVariavel, Nome, ValoresReferencia)
VALUES
(0, 'Hemoglobina', '13.8-17.2 g/dL (homens), 12.1-15.1 g/dL (mulheres)'),
(1, 'Hematócrito', '40.7-50.3% (homens), 36.1-44.3% (mulheres)'),
(2, 'Leucócitos (WBC)', '4,500-11,000 células/µL'),
(3, 'Plaquetas', '150,000-450,000/µL'),
(4, 'Glicose', '70-99 mg/dL (jejum)'),
(5, 'Creatinina', '0.7-1.3 mg/dL (homens), 0.6-1.1 mg/dL (mulheres)'),
(6, 'Ureia', '6-20 mg/dL'),
(7, 'Colesterol Total', 'menor que 200 mg/dL'),
(8, 'LDL (Colesterol Ruim)', 'menor que 100 mg/dL'),
(9, 'HDL (Colesterol Bom)', 'maior que 40 mg/dL (homens), maior que 50 mg/dL (mulheres)'),
(10, 'Triglicerídeos', 'menor que 150 mg/dL'),
(11, 'TSH', '0.4-4.0 mIU/L'),
(12, 'T4 Livre', '0.8-1.8 ng/dL'),
(13, 'Ferro', '60-170 µg/dL'),
(14, 'Transferrina', '200-350 mg/dL'),
(15, 'Ferritina', '24-336 ng/mL (homens), 11-307 ng/mL (mulheres)'),
(16, 'Ácido Úrico', '3.4-7.0 mg/dL (homens), 2.4-6.0 mg/dL (mulheres)'),
(17, 'Bilirrubina Total', '0.1-1.2 mg/dL'),
(18, 'AST (TGO)', '10-40 U/L'),
(19, 'ALT (TGP)', '7-56 U/L');

INSERT INTO Arquivo
(CodArquivo, Nome, Tipo, Conteudo)
VALUES
(0, 'laudo-0.pdf', 'PDF', "teste"),
(1, 'laudo-1.rtf', 'RTF', "teste"),
(2, 'exame-2.png', 'PNG', "teste"),
(3, 'exame-3.png', 'PNG', "teste"),
(4, 'laudo-4.pdf', 'PDF', "teste"),
(5, 'exame-5.jpg', 'JPG', "teste"),
(6, 'exame-6.jpg', 'JPG', "teste"),
(7, 'exame-7.png', 'PNG', "teste"),
(8, 'exame-8.png', 'PNG', "teste"),
(9, 'exame-9.png', 'PNG', "teste"),
(10, 'exame-10.png', 'PNG', "teste"),
(11, 'laudo-11.pdf', 'PDF', "teste");

INSERT INTO Exame
(CodExame, CodPaciente, CodConsulta_Prescricao, TipoEspecializacao, DataHora, Motivo, Tipo, CondicoesCooperacao, Orgaos, CodArquivo_Laudo)
VALUES
(0, 7, 13, 1, '2025-02-14T02:17:28.328925', 'Laudo', 'Aspernatur maxime a quod aut non necessitatibus. Rerum maiores voluptates similique blanditiis et.\nQuasi accusantium suscipit deserunt.', "OK", NULL, 0),
(1, 1, 8, 1, '2025-01-27T08:52:33.805562', 'Laudo', 'Deleniti harum facere commodi expedita. Illo porro tempore eum. Quia possimus labore similique modi illo quos.\nOfficia atque repudiandae. Facere atque voluptas culpa maxime rem.', "OK", NULL, 1),
(2, 0, NULL, 2, '2025-01-26T08:33:09.339137', "Exame de Sangue", 'Odit doloribus soluta numquam. Laboriosam suscipit perspiciatis.\nDolores eligendi cumque dolores dolorem.', "OK", NULL, NULL),
(3, 3, 0, 0, '2025-01-26T09:08:11.509041', 'Tomografia por Emissão de Positrons (PET)', 'Ratione in necessitatibus placeat quae ullam. Magni modi asperiores illum omnis vitae.\nDoloribus fugit totam dolores laboriosam ullam. Saepe voluptatum suscipit fuga. Nobis quod soluta.', 'Paciente não realizou o jejum indicado antes do exame de sangue.', 'Ouvidos', NULL),
(4, 8, 11, 1, '2025-02-18T16:28:56.786784', 'Laudo', 'Iure cumque labore culpa ullam sint quis beatae. Exercitationem occaecati quisquam occaecati quidem deserunt. Debitis nesciunt eos odio enim.', "OK", NULL, 4),
(5, 5, NULL, 0, '2025-01-28T04:10:13.218719', 'Tomografia por Emissão de Positrons (PET)', 'Minima reprehenderit explicabo. Quasi quaerat excepturi blanditiis vitae sequi illum sint.\nOccaecati voluptas modi corporis fugiat qui. Esse sunt voluptatibus expedita veniam maiores vitae.', "OK", 'Intestino Grosso', NULL),
(6, 6, 3, 0, '2025-02-02T00:32:39.659433', 'Tomografia Computadorizada (TC)', 'Repellat dolorem culpa mollitia tempora quos magni. Ad officia cumque voluptatibus.', 'Não foi realizada a ingestão adequada de água antes do ultrassom abdominal.', 'Ouvidos', NULL),
(7, 2, 7, 0, '2025-02-02T18:32:30.011091', 'Mamografia', 'Dolorem facilis esse non. Itaque vitae laboriosam necessitatibus.\nAt laboriosam repellendus eos facere atque omnis. Reprehenderit consequatur nam ab. Nam quidem laudantium porro ut nam.', 'Relatou ter ingerido alimentos gordurosos na noite anterior ao teste de colesterol.', 'Intestino Delgado', NULL),
(8, 3, 2, 1, '2025-02-16T18:31:22.832482', 'Laudo', 'Enim dicta quod optio quos. Fugit consectetur quod illo magnam.', "OK", NULL, 11),
(9, 7, 13, 2, '2025-02-05T22:17:45.554107', "Exame de Sangue", 'Voluptate iure iure vel voluptatum repudiandae. Perferendis magnam laborum et placeat.\nEt tempora dolorem voluptas voluptates nemo aliquam. Ea quas debitis debitis.', 'O consentimento informado foi assinado e todas as informações foram compreendidas pelo paciente.', NULL, NULL);

INSERT INTO ArquivoExameImagem
(CodArquivo, CodExame, CodAEI)
VALUES
(2, 3, 0),
(3, 3, 1),
(5, 5, 0),
(6, 5, 1),
(7, 5, 2),
(8, 6, 0),
(9, 6, 1),
(10, 7, 0);

INSERT INTO VariavelExameQuantitativo
(CodVariavel, CodExame, CodVEQ, Valor, MetodoAnalise)
VALUES
(11, 2, 0, 17.790766067776254, 'Ensaio de Ligação Competitiva'),
(7, 2, 1, 81.90066990688626, 'Eletroforese'),
(19, 2, 2, 89.34350918478603, 'Cromatografia Líquida de Alta Eficiência (HPLC)'),
(0, 2, 3, 20.479079826935, 'Turbidimetria'),
(9, 9, 0, 63.69660374117204, 'Eletroforese'),
(7, 9, 1, 44.481115514620384, 'Radioimunoensaio'),
(16, 9, 2, 5.7857113901017225, 'Quimioluminescência'),
(0, 9, 3, 41.72254797962051, 'Potenciometria');

INSERT INTO Dispositivo
(CodDispositivo, ChaveSeguranca, Tipo)
VALUES
(0, '3Bx7flggLjR5lAk7vGwNfUsZBCnh8sLA', 'Tablets para Ambulâncias'),
(1, 'fE7HzNbqPay3SBUv2PmfeqHh13Ve1riG', 'Desktop'),
(2, 'GzNzWWsxMjRxKiPvDzDRtOdsUdMbD3aG', 'Laptop'),
(3, 'Qf65ywhaqNs3iJlASxuOQj5jtmlv8AET', 'Desktop'),
(4, 'BmS4cN2wUQosf1UV2zdRPOHTACpDucdv', 'Celular'),
(5, 'OiWQ8y5Cvg2XuCubcwmGlmPTt1pvSc5e', 'Tablets para Ambulâncias'),
(6, 'EB4zEBfoZj2nLYI2y7pn0rv9g3LWSWFC', 'Celular');

INSERT INTO AcessoBD
(CodAcesso, CodProfissional, CodDispositivo, NivelAutorizacao, NomeUsuario, Senha)
VALUES
(0, 4, 1, 'Read', 'iazevedo', 'GlHGiX7n#3'),
(1, 1, 4, 'Write', 'da-cunhagustavo', 'd1IGUa2a+*'),
(2, 1, 1, 'Write', 'vnovaes', '^Pm6LDIm#r'),
(3, 6, 1, 'Read', 'qda-costa', '*7Eu+hc1vY'),
(4, 4, 5, 'Write', 'fariaslorenzo', 'I2Vklxgc*6'),
(5, 0, 5, 'Write', 'marinaribeiro', '#3WBT!o5)X'),
(6, 8, 3, 'Read', 'marina32', 'KKb8MLhw^H');

INSERT INTO RegistroAcesso
(CodRegistroAcesso, CodAcesso, CodProfissional, CodDispositivo, CodPaciente, DataHora, CRUouD, Tabelas, CodigoRegistroAfetado)
VALUES
(0, 0, 6, 5, 4, '2025-02-12T01:49:55.510064', 'C', 'Especialidade, Arquivo, Remedio', 2),
(1, 1, 3, 0, 8, '2025-01-22T14:06:59.875102', 'U', 'Especialidade, Medicacao, ProfissionalSaude', 1),
(2, 1, 0, 4, 8, '2025-01-28T04:04:07.198841', 'U', 'NomeComercialRemedio, Paciente, Cirurgia', 3),
(3, 1, 2, 4, 1, '2025-02-16T13:36:01.591404', 'R', 'ArquivoExameImagem, ArquivoExameImagem', 4),
(4, 6, 3, 1, 2, '2025-02-08T12:20:14.549124', 'R', 'Consulta, NomeComercialRemedio, Medicacao, Dispositivo', 0),
(5, 4, 0, 4, 9, '2025-02-17T04:00:36.870045', 'U', 'Vacina, Paciente, Especialidade, Exame', 3),
(6, 6, 7, 4, 5, '2025-02-03T07:00:13.153086', 'C', 'Alergia, Diagnostico, AlergiaPaciente', 2),
(7, 6, 4, 3, 0, '2025-01-28T06:19:59.553086', 'R', 'ProfissionalParticipanteCirurgia', 1),
(8, 2, 7, 5, 3, '2025-01-22T01:46:39.760059', 'U', 'Exame, ProfissionalParticipanteCirurgia, Consulta', 4),
(9, 0, 2, 2, 0, '2025-02-20T19:57:10.089282', 'D', 'Paciente', 0);

