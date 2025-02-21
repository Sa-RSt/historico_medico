Para executar o programa, crie um virtualenv do python usando:
    python3 -m venv .venv

Ative-o:
    source .venv/bin/activate  # linux
    .\.venv\Scripts\activate  # windows

Instale as dependências:
    pip install -r requirements.txt

Execute o programa:
    fastapi dev backend.py


Organização do projeto:
    public/  - Arquivos públicos servidos pelo servidor (html, css e js)
    backend.py  - Lógica do backend contida em um só arquivo.
    config.json  - Edite esse arquivo para colocar as configurações do SGBD (nome do banco de dados, usuário, senha, porta, host)
    criar_tabelas.sql  - Arquivo que cria as tabelas no banco de dados.
    dados.sql  - Arquivo que contém dados de exemplo.
    requirements.txt  - Dependências para instalar com o pip.
