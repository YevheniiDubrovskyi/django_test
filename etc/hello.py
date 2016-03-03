bind = '0.0.0.0:8080'
pythonpath = '/home/box/web/etc'

def app(environ, start_response):
	data = environ('QUERY_STRING').split('&').join('\n')
	status = '200 OK'
	response_headers = [
		('Content-type','text/plain'),
		('Content-length', str(len(data)))
	]
	start_response(status, response_headrs)
	return iter([data])
