import os, sys
os.chdir('/Users/shashikant/Desktop/Visioneerit/News_Build/News-plan')
import http.server, socketserver
PORT = 3333
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
