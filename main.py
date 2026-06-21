from funcoes import buscar_contatos, enviar_mensagem
import logging

# Configurar logger
logging.basicConfig(level=logging.INFO)


# Fluxo principal do projeto.
def main():
    contatos = buscar_contatos()
    if not contatos:
        logging.warning("Nenhum contato encontrado. Encerrando execução.")
        return

    for contato in contatos:
        enviar_mensagem(contato)


if __name__ == "__main__":
    main()
