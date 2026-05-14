from fastapi.responses import RedirectResponse
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from model import (
    consulta_hospedes,
    add_hospede,
    consulta_hospede_id,
    update_hospede,
    delete_hospede,
    consulta_quartos,
    add_quarto,
    consulta_quarto_id,
    update_quarto,
    delete_quarto,
    consulta_reservas,
    add_reserva,
    delete_reserva
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

@app.get("/quartos")
def quartos(request: Request):

    quartos = consulta_quartos()

    return templates.TemplateResponse(
        request=request,
        name="quartos.html",
        context={
            "quartos": quartos
        }
    )

@app.get("/add_quarto")
def add_quarto_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="add_quarto.html"
    )

@app.post("/add_quarto")
def salvar_quarto(
    numero: str = Form(),
    tipo: str = Form(),
    valor_diaria: float = Form(),
    status: str = Form()
):

    add_quarto(
        numero,
        tipo,
        valor_diaria,
        status
    )

    return RedirectResponse(
        url="/quartos",
        status_code=303
    )

@app.get("/edit_quarto/{id}")
def edit_quarto(request: Request, id: int):

    quarto = consulta_quarto_id(id)

    return templates.TemplateResponse(
        request=request,
        name="edit_quarto.html",
        context={
            "quarto": quarto
        }
    )

@app.post("/edit_quarto/{id}")
def salvar_edicao_quarto(
    id: int,
    numero: str = Form(),
    tipo: str = Form(),
    valor_diaria: float = Form(),
    status: str = Form()
):

    update_quarto(
        id,
        numero,
        tipo,
        valor_diaria,
        status
    )

    return RedirectResponse(
        url="/quartos",
        status_code=303
    )

@app.get("/delete_quarto/{id}")
def excluir_quarto(id: int):

    delete_quarto(id)

    return RedirectResponse(
        url="/quartos",
        status_code=303
    )

@app.get("/reservas")
def reservas(request: Request):

    reservas = consulta_reservas()

    return templates.TemplateResponse(
        request=request,
        name="reservas.html",
        context={
            "reservas": reservas
        }
    )

@app.get("/add_reserva")
def add_reserva_page(request: Request):

    hospedes = consulta_hospedes()

    quartos = consulta_quartos()

    return templates.TemplateResponse(
        request=request,
        name="add_reserva.html",
        context={
            "hospedes": hospedes,
            "quartos": quartos
        }
    )

@app.post("/add_reserva")
def salvar_reserva(
    hospede_id: int = Form(),
    quarto_id: int = Form(),
    data_entrada: str = Form(),
    data_saida: str = Form()
):

    add_reserva(
        hospede_id,
        quarto_id,
        data_entrada,
        data_saida
    )

    return RedirectResponse(
        url="/reservas",
        status_code=303
    )

@app.get("/delete_reserva/{id}")
def excluir_reserva(id: int):

    delete_reserva(id)

    return RedirectResponse(
        url="/reservas",
        status_code=303
    )