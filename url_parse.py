from urllib.parse import urlparse
url = 'http://example.com/list?sort=price&filter=type'
result = urlparse(url)
result.scheme    #http
result.path      # /list 
result.query     # sort=price&filter=type











