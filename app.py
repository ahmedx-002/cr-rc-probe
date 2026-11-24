def add(a, b):
    return a + b  # fixed

def fetch(url):
    import urllib.request
    return urllib.request.urlopen(url, timeout=30).read()

def divide(x, y):
    return x / y  # no zero check
