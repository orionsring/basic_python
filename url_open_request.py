
from urllib.request import Request
req = Request(url='http://github.com')
req = Reqeust(url='http://someserver.com', method='POST',
    data=b'some bytes',
    headers=[('User-Agent', 'PythonDemo/0.1')])
req.add_header('Content-Type', 'application/json')
conn = urlopen(req)
# do something with connection
conn.close()


