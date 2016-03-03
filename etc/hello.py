def app(environ, start_response)
	data = ''
	status = '200 OK'
	response_headers = [
		('Content-type','text/plain'),
		('COntent-length', str(len(data)))
	]
	start_response(status, response_headrs)
	return iter([data])
