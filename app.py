from flask import redirect
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from logger import logger
from sqlalchemy import select

from model import Session, Anuncio
from schemas import *

info = Info(title="API de Anúncios de veículos da Moove-se", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
anuncios_tag = Tag(name="Anúncios", description="Visualização dos anúncios")

################################################################################
# GET
################################################################################


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.get('/anuncios', tags=[anuncios_tag],
         responses={"200": ListaAnunciosSchema, "404": ErrorSchema})
def get_anuncios():
    """Faz a busca por todos os Anúncios cadastrados
       Retorna uma representação da listagem de Anúncios.
    """

    try:

        logger.debug("Coletando Anúncios")

        session = Session()

        stmt = select(Anuncio)

        print(stmt)

        anuncios = session.execute(stmt).fetchall()

        if not anuncios:
            return {"anuncios": []}, 200
        else:
            logger.debug(f"%d Anúncios encontrados" % len(anuncios))
            print(anuncios)
            return show_anuncios(anuncios), 200

    except Exception as e:
        logger.warning(f"Erro ao obter os Anúncios, {e.__traceback__}")
        return {"message": e.__traceback__}, 500

app.run(port=5001, debug=True, use_reloader=True)