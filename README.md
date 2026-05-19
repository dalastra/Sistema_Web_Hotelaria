# 🏨 Sistema Web de Hotelaria

Sistema web desenvolvido com **FastAPI + MySQL + Jinja2**, permitindo o gerenciamento completo de:

- Hóspedes
- Quartos
- Reservas

O projeto possui CRUD completo, relacionamento entre tabelas e integração com banco de dados MySQL.

---

# 🚀 Tecnologias Utilizadas

- Python
- FastAPI
- MySQL
- PyMySQL
- Jinja2
- HTML
- CSS

---

# 📂 Estrutura do Projeto

```bash
Sistema_Web_Hotelaria/
│
├── static/
│   ├── css/
│       └── style.css
│
├── templates/
│   ├── index.html
│   ├── hospedes.html
│   ├── add_hospede.html
│   ├── edit_hospede.html
│   ├── quartos.html
│   ├── add_quarto.html
│   ├── edit_quarto.html
│   ├── reservas.html
│   ├── add_reserva.html
│   ├── edit_reserva.html
│   └── view_reserva.html
│
├── app.py
├── dao.py
├── model.py
└── README.md
```

---

# ⚙️ Funcionalidades

## 👤 Hóspedes
- Cadastrar hóspede
- Listar hóspedes
- Editar hóspedes
- Excluir hóspedes

## 🛏️ Quartos
- Cadastrar quarto
- Listar quartos
- Editar quartos
- Excluir quartos

## 📅 Reservas
- Cadastrar reservas
- Listar reservas
- Visualizar detalhes da reserva
- Editar reservas
- Excluir reservas

---

# 🗄️ Banco de Dados

O sistema utiliza MySQL com relacionamento entre tabelas.

## Relacionamentos

- Uma reserva pertence a um hóspede
- Uma reserva pertence a um quarto

Utilizando:
- FOREIGN KEY
- INNER JOIN

---

# ▶️ Como Executar o Projeto

## 1️⃣ Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
```

---

## 2️⃣ Entrar na pasta

```bash
cd Sistema_Web_Hotelaria
```

---

## 3️⃣ Criar ambiente virtual

### Windows

```bash
python -m venv venv
```

---

## 4️⃣ Ativar ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

---

## 5️⃣ Instalar dependências

```bash
pip install fastapi
pip install "uvicorn[standard]"
pip install jinja2
pip install python-multipart
pip install pymysql
```

---

# 🛠️ Configurar Banco de Dados

## Criar banco

```sql
CREATE DATABASE hotelaria;
```

---

## Criar tabela hóspedes

```sql
CREATE TABLE hospedes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(20),
    cpf VARCHAR(20)
);
```

---

## Criar tabela quartos

```sql
CREATE TABLE quartos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    numero VARCHAR(10),
    tipo VARCHAR(50),
    valor_diaria DECIMAL(10,2)
);
```

---

## Criar tabela reservas

```sql
CREATE TABLE reservas (
    id INT PRIMARY KEY AUTO_INCREMENT,

    hospede_id INT,
    quarto_id INT,

    data_entrada DATE,
    data_saida DATE,

    FOREIGN KEY (hospede_id)
    REFERENCES hospedes(id),

    FOREIGN KEY (quarto_id)
    REFERENCES quartos(id)
);
```

---

# 🔌 Configurar conexão MySQL

No arquivo `model.py`, altere os dados da conexão:

```python
pymysql.connect(
    host="localhost",
    user="root",
    password="SUA_SENHA",
    database="hotelaria"
)
```

---

# ▶️ Executar o sistema

```bash
fastapi dev
```

---

# 🌐 Acessar no navegador

```txt
http://127.0.0.1:8000
```

---

# 📸 Funcionalidades do Sistema

✅ CRUD completo  
✅ Banco relacional  
✅ Sistema de reservas  
✅ Relacionamento entre tabelas  
✅ JOINs SQL  
✅ Templates dinâmicos com Jinja2  
✅ CSS integrado  
✅ Navegação entre páginas  

---

# 📚 Conceitos Aplicados

- FastAPI
- CRUD
- MVC
- Jinja2
- MySQL
- Relacionamentos SQL
- Foreign Key
- INNER JOIN
- Rotas GET e POST
- Templates HTML
- CSS
- Backend Web

---

# 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos e aprendizado de desenvolvimento web com FastAPI.
