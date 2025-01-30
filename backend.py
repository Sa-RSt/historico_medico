from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import mariadb
import logging
import string
from pydantic import BaseModel


class Profissional(BaseModel):
    id: int
    crm: str | None
    nome_social: str | None
    nome_civil: str
    profissao: str


class ResultadoConsulta(BaseModel):
    erro: str | None
    resultado: list[Profissional] | None


app = FastAPI()
BASE_DIRECTORY = Path(__file__).parent
app.mount('/static', StaticFiles(directory=BASE_DIRECTORY / 'static'), name='static')
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('historico_medico')
LEGAL_PAGE_NAME_CHARS = string.ascii_letters + string.digits + '-_'

@app.get('/', response_class=HTMLResponse)
def index():
    '''Acessa a página index.'''
    return HTMLResponse((BASE_DIRECTORY / 'index.html').read_text())

@app.get('/{path}', response_class=HTMLResponse)
def page(path):
    f'''Acessa uma página HTML. Os caracteres permitidos no nome da página são: {LEGAL_PAGE_NAME_CHARS}'''
    filtered_path = (BASE_DIRECTORY / ''.join(x for x in path if x in LEGAL_PAGE_NAME_CHARS)).with_suffix('.html')
    if not filtered_path.exists():
        return HTMLResponse('<h1>404 not found</h1>', 404)
    return HTMLResponse(filtered_path.read_text())

@app.get('/api/medicos')
def medicos() -> ResultadoConsulta:
    '''Lista todos os médicos.'''
    try:
        conn = mariadb.connect(
            user="app",
            password="123456",
            host="localhost",
            port=3306,
            database="historico_medico"
        )
    except Exception as e:
        log.exception(e)
        return ResultadoConsulta(erro='falha ao conectar ao banco de dados', resultado=None)
    cur = conn.cursor()
    cur.execute('SELECT * FROM ProfissionalSaude;')
    result_set = []
    for CodProfissional, CRM, NomeSocial, NomeCivil, Profissao in cur:
        result_set.append(Profissional(
            id=CodProfissional,
            crm=CRM,
            nome_social=NomeSocial,
            nome_civil=NomeCivil,
            profissao=Profissao
        ))
    return ResultadoConsulta(erro=None, resultado=result_set)
