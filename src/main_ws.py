import sys
from src.webservice.ws_server_core import ws_server_core

if __name__ == "__main__":
    args = sys.argv[1:]
    server = ws_server_core(args[0])

    server.start()