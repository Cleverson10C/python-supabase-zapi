# Supabase + Z-API Python

Projeto desenvolvido como parte do desafio de estágio em Desenvolvimento Python.
O objetivo é integrar **Supabase** (banco de dados) com **Z-API** (WhatsApp) para envio de mensagens personalizadas.

---

## Setup da Tabela no Supabase

Crie a tabela `contatos` no Supabase utilizando o seguinte SQL:

```sql
create table contatos (
  id bigint generated always as identity primary key,
  nome_contato text not null,
  telefone text not null
);

insert into contatos (nome_contato, telefone)
values 
('José', '5541991356580'),
('Maria', '5541991089192');
```

---

## Configuração de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
SUPABASE_URL=https://<seu-projeto>.supabase.co
SUPABASE_KEY=<sua-chave-publica>
ZAPI_ID=<id-da-instancia-zapi>
ZAPI_TOKEN=<token-da-instancia-zapi>
```

---

## Instalação

Clone o repositório:

```
https://github.com/Cleverson10C/python-supabase-zapi.git
cd supabase-zapi-python
```

Crie e ative o ambiente virtual:

```
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

Instale as dependências:

```
pip install -r requirements.txt
```

---

## Execução

Para rodar o projeto:

```
python main.py
```
