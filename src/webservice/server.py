from bottle import Bottle
from src.commons.utils.configuration_loader import configuration_loader
from src.webservice.route_loader import route_loader


class server(object):

    def __init__(self, json):
        self._app = Bottle()
        self.config = configuration_loader(json)
        routes = route_loader(self._app, self.config.mongo_datas)
        routes.load_all_route()

    def start(self):
        self._app.run(host="localhost", port=8080)
