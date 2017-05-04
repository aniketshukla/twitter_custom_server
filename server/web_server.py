'''
Basic http server
Only handles get request
To create a handler for new request add a do_* method * being the request type
for a post request handler do_POST
'''

import BaseHTTPServer
import SocketServer
import json
path_to_function={}



def router(path):
    '''decorator to add new routes'''
    def router_method(func):
        print(__name__)
        path_to_function[path]=func
        return func
    return router_method


def route(path,func):
    '''alternative to decorator'''
    path_to_function[path]=func
    return func

'''adding default routes'''
route('404',lambda :'{error:404}')



class Handler(object,BaseHTTPServer.BaseHTTPRequestHandler):
    #extends simpleHTTPRequestHandler
    def __init__(self,*args):
        BaseHTTPServer.BaseHTTPRequestHandler.__init__(self,*args)
        #adding default 404 route here



    def response_handler(self,result,response_code=200,
                        response_type='application/json'):
        '''This function sends response to client'''
        self.send_response(response_code)
        self.send_header("Content-type", response_type)
        self.send_header("Content-Length", len(result))
        self.end_headers()
        self.wfile.write(result)



    def do_GET(self):
        '''
        This function handles the get request
        Path of the request is checked
        If a path to function mapping is available ,the function is called
        else
        server returns a 500 error
        Content-type json
        '''



        try:
            response=path_to_function[self.path]()
            self.response_handler(response,200)
            return
        except Exception as err:
            response=path_to_function['404']()
            self.response_handler(response,404)
            return



class Server:
    '''associates server and handler'''

    def __init__(self):
        self.handler=Handler



    def run_server(self,PORT=80,HOST="0.0.0.0"):
        print(PORT)
        httpd=SocketServer.TCPServer((HOST, PORT), self.handler)
        httpd.serve_forever()
