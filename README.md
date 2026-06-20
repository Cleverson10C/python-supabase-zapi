# Supabase + Z-API Python 

Projeto desenvolvido como parte do desafio de estágio em Desenvolvimento Python.  
O objetivo é integrar **Supabase** (banco de dados) com **Z-API** (WhatsApp) para enviar mensagens personalizadas.

## Setup da Tabela no Supabase
Crie a tabela `contatos` no Supabase usando o SQL abaixo:

```sql
create table contatos (
  id bigint generated always as identity primary key,
  nome_contato text not null,
  telefone text not null
);

insert into contatos (nome_contato, telefone)
values 
('Cleverson', '5541992356589'),
('Lucimara', '5541992089191');

Crie um arquivo .env na raiz do projeto com
SUPABASE_URL=https://<seu-projeto>.supabase.co
SUPABASE_KEY=<sua-chave-publica>
ZAPI_ID=<id-da-instancia-zapi>
ZAPI_TOKEN=<token-da-instancia-zapi>

Instalação
Clone o repositório:
https://github.com/Cleverson10C/python-supabase-zapi.git
cd supabase-zapi-python

Crie e ative o ambiente virtual:
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

Instale as dependências:
pip install -r requirements.txt

Para rodar o projeto:
python main.py
