import os
import logging
import requests
from supabase import create_client, Client
from dotenv import load_dotenv
from logger_config import setup_logger

# Carregar variáveis de ambiente do .env
load_dotenv()


# Configurar logger
logging = setup_logger()


# Variáveis de ambiente
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_ID = os.getenv("ZAPI_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")


# Criar cliente Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# # Busca todos os contatos da tabela 'contatos' no Supabase.
def buscar_contatos():
    try:
        response = supabase.table("contatos").select("*").execute()
        contatos = response.data
        logging.info(f"{len(contatos)} contatos encontrados no Supabase.")
        return contatos
    except Exception as e:
        logging.error(f"Erro ao buscar contatos: {e}")
        return []


# Envia mensagem personalizada via Z-API.
def enviar_mensagem(contato):
    try:
        url = f"https://api.z-api.io/instances/{ZAPI_ID}/token/{ZAPI_TOKEN}/send-text"
        headers = {
          "Content-Type": "application/json"
   }
        mensagem = f"Olá, {contato['nome_contato']} tudo bem com você?"
        payload = {
             "phone": contato["telefone"],
             "message": mensagem
         }
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            logging.info(f"Mensagem enviada para {contato['nome_contato']} ({contato['telefone']}).")
        else:
            logging.error(f"Falha ao enviar para {contato['nome_contato']}: {response.text}")
    except Exception as e:
        logging.error(f"Erro ao enviar mensagem: {e}")