from http import server
import socket

class HTTPRequestHandler(server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # The idea is to use <RCPT TO> value to choose and connect to different mail server
        print(self.headers)
        rcpt_to_header = self.headers['Auth-SMTP-To']
        rcpt_to = rcpt_to_header.split(":")[1][2:-1]
        self.send_custom_headers(rcpt_to)
        server.SimpleHTTPRequestHandler.end_headers(self)

    def send_custom_headers(self, rcpt):
        # This is a simple logic to choose mail server  
        if rcpt.split("@")[1] == "eng.abc.com":
            self.send_header("Auth-Status", "OK")
            self.send_header("Auth-Server", socket.gethostbyname('postfix-1'))
            self.send_header("Auth-Port", "25")
        elif rcpt.split("@")[1] == "hr.abc.com":
            self.send_header("Auth-Status", "OK")
            self.send_header("Auth-Server", socket.gethostbyname('postfix-2'))
            self.send_header("Auth-Port", "25")        


if __name__ == '__main__':
    server.test(HandlerClass=HTTPRequestHandler)
