#sudo gunicorn -c /etc/gunicorn.d/hello.py hello:app

def app(environ, start_response):
	data = '\r\n'.join(environ['QUERY_STRING'].split('&'))
	status = '200 OK'
	response_headers = [
		('Content-type','text/plain'),
		('Content-length', str(len(data)))
	]
	start_response(status, response_headers)
	return [data]
