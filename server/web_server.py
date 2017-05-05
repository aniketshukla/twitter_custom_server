'''
Basic http server
Only handles get request
To create a handler for new request add a do_* method * being the request type
for a post request handler do_POST
'''



import BaseHTTPServer
import SocketServer
import json
from jinja2 import Environment, PackageLoader, select_autoescape
import os



#global variables
path_to_function={}
path_to_responseType={}
env=Environment(
            loader=PackageLoader('public', 'templates',encoding='utf-8'),
            autoescape=select_autoescape(['html', 'xml'])
            )



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
        If the path starts with /public the file availabilty is checked in the public folder and returned if available
        If a path to function mapping is available ,the function is called
        else
        server returns a 500 error
        Content-type json
        '''

        if self.path[0:7]=='/public':
            try:
                path_new=os.path.join(os.getcwd(),self.path)
                response=open(os.getcwd()+self.path).readlines()
                self.response_handler(''.join(response),200,'')
                return
            except:
                '''goes to 404 for execution'''
                1

        try:
            response=path_to_function[self.path]()
            self.response_handler(response['data'],200,response['type'])
            return
        except Exception as err:
            print(err)
            response=path_to_function['404']()
            self.response_handler(response,404)
            return



class Server:
    '''associates server and handler'''

    def __init__(self):
        self.handler=Handler



    @staticmethod
    def render(template_path,**kwargs):
        '''renders template using jinja2 '''
        '''template path is the template html present in template folder and
        kwargs are the dictionary mapping for jinja2'''
        template=env.get_template(template_path)
        return {'data':template.render(**kwargs),'type':''}



    @staticmethod
    def send_data(response_dict):
        '''sends JSON response to the server'''
        return {'data':json.dumps(response_dict),'type':'application/json'}



    def run_server(self,PORT=80,HOST="0.0.0.0"):
        print(PORT)
        httpd=SocketServer.TCPServer((HOST, PORT), self.handler)
        httpd.serve_forever()
