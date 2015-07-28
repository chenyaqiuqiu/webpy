import random
import string

import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"
    @cherrypy.expose
    def post(self):
        return ''.join(random.sample(string.hexdigits, 8))

if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host':'127.0.0.1',
        'server.socket_port': 9999,
        })
    cherrypy.quickstart(HelloWorld())


