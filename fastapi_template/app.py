from http import HTTPStatus
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from fastapi_template.models.user import User
from fastapi_template.routers import auth, users
from fastapi_template.schemas.message import Message
from fastapi_template.security import get_current_user

CurrentUser = Annotated[User, Depends(get_current_user)]

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/docs')
async def get_documentation(current_user: CurrentUser):
    return get_swagger_ui_html(openapi_url='/openapi.json', title='docs')


@app.get('/openapi.json')
async def openapi(current_user: CurrentUser):
    return get_openapi(title='FastAPI', version='0.1.0', routes=app.routes)
