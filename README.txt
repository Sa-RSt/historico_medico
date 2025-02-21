Para executar o programa, crie um virtualenv do python usando:
    python3 -m venv .venv

Ative-o:
    source .venv/bin/activate  # linux
    .\.venv\Scripts\activate  # windows

Instale as dependências:
    pip install -r requirements.txt

Execute o programa:
    fastapi dev backend.py
