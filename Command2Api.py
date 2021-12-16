import subprocess
# import BaseHTTPServer
# import SimpleHTTPServer
import cgi
import threading
import sys
import string
import random
from http.server import HTTPServer, BaseHTTPRequestHandler

l = []
uri = "/getRecord"
checkuri = "/checkAlive"

class thread(threading.Thread):
	def __init__(self, threadname, command):
		threading.Thread.__init__(self, name='Thread_' + threadname)
		self.threadname = int(threadname)
		self.command = command

	def run(self):
		global l
		ret = subprocess.Popen(
			self.command,
			shell=True,
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE
		)
		for i in iter(ret.stdout.readline, b""):
			l.append(i.decode().strip())
			print(l)

class ServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		global l
		if self.path == uri:
			lstr = "\n".join(l)
			self.send_response(200)
			self.send_header('Content-type', 'application/json')
			self.end_headers()
			self.wfile.write(lstr.encode())
		if self.path == checkuri:
			self.send_response(200)
			self.send_header('Content-type', 'application/json')
			self.end_headers()
			msg = "commandAPI works!"
			self.wfile.write(msg.encode())

if __name__ == '__main__':
	print("***Command2API for local LDAP check***")
	print("Usage:python3 Command2Api.py yourCommand APIPort")
	t1 = thread('1', sys.argv[1])
	t1.start()
	port = int(sys.argv[2])
	print("URL: http://{0}:{1}{2}".format("127.0.0.1",port, uri))
	Handler = ServerHandler
	httpd = HTTPServer(('0.0.0.0', port), Handler)
	httpd.serve_forever()
