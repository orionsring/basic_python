from urllib.parse import urlparse
url = 'http://example.com/list?sort=price&filter=type'
result = urlparse(url)
result.scheme    #http
result.path      # /list 
result.query     # sort=price&filter=type

from urllib.parse import urlparse, parse_qs
url = 'http://example.com/list?sort=price&filter=type'
result = urlparse(url)
qs_data= parse_qs(result.query)









