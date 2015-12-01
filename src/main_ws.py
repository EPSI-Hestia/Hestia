import sys
from src.webservice.server import server

if __name__ == "__main__":
    args = sys.argv[1:]
    server = server(args[0]);
    server.start();
