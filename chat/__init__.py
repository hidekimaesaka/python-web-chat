from chat.handler import ChatHandler

from chat.server import ThreadedTCPServer


def start_server(host: str, port: int) -> None:
    host = str(host)
    port = int(port)

    with ThreadedTCPServer((host, port), ChatHandler) as server:
        try:
            print(f"Servidor rodando em {host}:{port}")
            server.serve_forever()

        except Exception as e:
            print(__name__, e)
            server.server_close()
