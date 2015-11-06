# -*- coding: utf-8 -*-

from bottle import *
import os


@error(404)
def notfound(error):
    return "<h1>Nothing to see here</h1>"

@error(500)
def error_server():
    return "<h1>erreur du serveur</h1>"

@error(400)
def error400():
    return "<h1> 400 - Bad request</h1>"

@get('/<boardname>/<agentname>/read/<value>')
def badurl(boardname, agentname, value):
    error400()

@get('/<boardname>/<agentname>/write')
def badurl(boardname, agentname):
    return error400()


@get('/boards')
def board_list():
    return "liste des boards : "

@get('/<boardname>')
def agent_list(boardname):
    return ("Etat de la board: %s avec la liste des agents : " % boardname)

@get('/<boardname>/<agentname>/write/<value>')
def write_last_agent_value(boardname, agentname, value):
    return "board : " + boardname + ", permet d'écrire la derniere valeur " + value + " de l'agent : " + agentname 

@get('/<boardname>/<agentname>/read')
def read_last_agent_value(boardname, agentname):
    return " board : " + boardname + ", permet de lire la derniere valeur de l'agent : " + agentname 

@get('/<boardname>/<agentname>read/last/<number:int>')
def read_last_number_agent_value(boardname, agentname, number):
    return "board : " + boardname + ", permet de lire la ou les " + number + " derniere(s) valeur(s) lu par l'agent : " + agentname

@get('/<boardname>/<agentname>/read/first/<number:int>')
def read_first_number_agent_value(boardname, agentname, number):
     return "board : " + boardname + ", permet de lire la ou les " + number + " premiere(s) valeur(s) lu par l'agent : " + agentname

run( debug=True, reloader=True)