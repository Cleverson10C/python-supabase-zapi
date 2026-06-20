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


def buscar_contatos():
    """Busca até 2 contatos da tabela 'contatos' no Supabase."""
    try:
        response = supabase.table("contatos").select("*").execute()
        contatos = response.data
        logging.info(f"{len(contatos)} contatos encontrados no Supabase.")
        return contatos
    except Exception as e:
        logging.error(f"Erro ao buscar contatos: {e}")
        return []


def enviar_mensagem(contato):
    """Envia mensagem personalizada via Z-API."""
    try:
        url = f"https://api.z-api.io/instances/{ZAPI_ID}/token/{ZAPI_TOKEN}/send-text"
        mensagem = f"Olá, {contato['nome_contato']} tudo bem com você?"
        payload = {
            "phone": contato["telefone"],
            "message": mensagem
        }
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            logging.info(f"Mensagem enviada para {contato['nome_contato']} ({contato['telefone']}).")
        else:
            logging.error(f"Falha ao enviar para {contato['nome_contato']}: {response.text}")
    except Exception as e:
        logging.error(f"Erro ao enviar mensagem: {e}")


def main():
    """Fluxo principal do projeto."""
    contatos = buscar_contatos()
    if not contatos:
        logging.warning("Nenhum contato encontrado. Encerrando execução.")
        return

    for contato in contatos:
        enviar_mensagem(contato)


if __name__ == "__main__":
    main()
