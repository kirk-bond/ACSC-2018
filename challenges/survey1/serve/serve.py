import SimpleHTTPServer
import BaseHTTPServer

def main():
    request_handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    request_handler.server_version = "acsc18{webheader_owngoal}"
    BaseHTTPServer.test(HandlerClass = request_handler, ServerClass = BaseHTTPServer.HTTPServer)
    
if __name__ == "__main__":
    main()
