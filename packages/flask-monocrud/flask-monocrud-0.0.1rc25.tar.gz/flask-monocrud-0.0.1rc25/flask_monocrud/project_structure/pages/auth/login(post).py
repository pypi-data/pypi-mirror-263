from flask import request
from flask_orphus.http import Session, Redirect, Request
from flask_orphus.routing.fs_router import endpoint
from flask_orphus import Request as orequest

from application.services.ADAuth import ADAuth


@endpoint(name="do_login")
def do_login():
    username = orequest.input('username')
    password = orequest.input('password')
    return ADAuth.raven_driver(username, password)
