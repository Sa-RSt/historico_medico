from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import mariadb
import logging
import string
from pydantic import BaseModel
import json

class Profissional(BaseModel):
    id: int
    crm: str | None
    nome_social: str | None
    nome_civil: str
    profissao: str


class ResultadoConsulta(BaseModel):
    erro: str | None
    resultado: list[Profissional] | None


with open('config.json', 'r') as file:
    CONFIG = json.load(file)

app = FastAPI()
BASE_DIRECTORY = Path(__file__).parent
PUBLIC_DIRECTORY = BASE_DIRECTORY / 'public'
STATIC_DIRECTORY = PUBLIC_DIRECTORY / 'static'
app.mount('/static', StaticFiles(directory=STATIC_DIRECTORY), name='static')
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('historico_medico')
LEGAL_PAGE_NAME_CHARS = string.ascii_letters + string.digits + '-_'

@app.get('/api/medicos')
def medicos() -> ResultadoConsulta:
    '''Lista todos os médicos.'''
    try:
        conn = mariadb.connect(**CONFIG['db_server'])
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


@app.get('/', response_class=HTMLResponse)
def index():
    f'''Acessa a página index.'''
    return HTMLResponse((PUBLIC_DIRECTORY / 'index.html').read_text())


@app.get('/{p:path}', response_class=HTMLResponse)
def page(p):
    f'''Acessa uma página.'''
    try:
        return HTMLResponse((PUBLIC_DIRECTORY / p).with_suffix('.html').read_text())
    except OSError:
        return HTMLResponse('', 404)
