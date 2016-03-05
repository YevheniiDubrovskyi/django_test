#sudo gunicorn -c /etc/gunicorn.d/hello.py hello:app

bind = '0.0.0.0:8080'
pythonpath = '/home/box/web'
python = '/usr/bin/pyhton'

def app(environ, start_response):
	data = '\r\n'.join(environ['QUERY_STRING'].split('&'))
	status = '200 OK'
	response_headers = [
		('Content-type','text/plain'),
		('Content-length', str(len(data)))
	]
	start_response(status, response_headers)
	return [data]
