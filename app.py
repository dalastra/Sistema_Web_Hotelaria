from fastapi.responses import RedirectResponse
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from model import (
    consulta_hospedes,
    add_hospede,
    consulta_hospede_id,
    update_hospede,
    delete_hospede
)
app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.get("/hospedes")
def home(request: Request):

    hospedes = consulta_hospedes()

    return templates.TemplateResponse(
    request=request,
    name="hospedes.html",
    context={
        "hospedes": hospedes
    }
)

@app.get("/add_hospede")
def add_hospede_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="add_hospede.html"
    )

@app.post("/add_hospede")
def salvar_hospede(
    nome: str = Form(),
    email: str = Form(),
    telefone: str = Form(),
    cpf: str = Form()
):

    add_hospede(nome, email, telefone, cpf)

    return RedirectResponse(
        url="/hospedes",
        status_code=303
    )

@app.get("/edit_hospede/{id}")
def edit_hospede(request: Request, id: int):

    hospede = consulta_hospede_id(id)

    return templates.TemplateResponse(
        request=request,
        name="edit_hospede.html",
        context={
            "hospede": hospede
        }
    )

@app.post("/edit_hospede/{id}")
def salvar_edicao_hospede(
    id: int,
    nome: str = Form(),
    email: str = Form(),
    telefone: str = Form(),
    cpf: str = Form()
):

    update_hospede(
        id,
        nome,
        email,
        telefone,
        cpf
    )

    return RedirectResponse(
        url="/hospedes",
        status_code=303
    )

@app.get("/delete_hospede/{id}")
def excluir_hospede(id: int):

    delete_hospede(id)

    return RedirectResponse(
        url="/hospedes",
        status_code=303
    )