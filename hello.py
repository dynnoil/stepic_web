from cgi import parse_qs


def application(environ, start_response):
    qs = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
    data = ''
    for param, value in qs.items():
        for elem in value:
            data += param + '='
            data += elem + '\r\n'
    status = '200 OK'   
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
