# Set the path for the SSL certificate and proxy settings  

# 1.1Before run the following code, check the exact name of certificate in your env by run the following in terminal
$ ls /etc/ssl/certs/

# 1.2cor run the following code directly in Jupyter Notebook
os.getenv("SSL_CERT_FILE")

# 1.3 or this is a whole way to check the "SSL_CERT_FILE"
if not os.getenv("SSL_CERT_FILE"):
    if not (cert := os.getenv("REQUESTS_CA_BUNDLE") or os.getenv("CURL_CA_BUNDLE")):
        cert = str(input("Please provide location to SSL certificate file:"))
    os.environ["SSL_CERT_FILE"] = cert

## If you want to check what kinds of env with "proxy" in your env. run the following in the terminal
$ env | grep -i 'proxy'


# In my case, it as ca_bundle.crt instead of ca-certificates.crt
# os.environ["SSL_CERT_FILE"] = "/etc/ssl/certs/ca-certificates.crt"  
os.environ["SSL_CERT_FILE"] = "/etc/ssl/certs/ca-bundle.crt"


# This is for setting the proxy
os.environ["HTTP_PROXY"] = "http://klientkache.3d.prci.com:8080"  
os.environ["HTTPS_PROXY"] = "http://klientkache.3d.prci.com:8080"  
os.environ["http_proxy"] = "http://klientkache.3d.prci.com:8080"  
os.environ["https_proxy"] = "http://klientkache.3d.prci.com:8080"  

os.environ["HTTP_PROXY"] = "http://servercache:55000"
os.environ["HTTPS_PROXY"] = "http://servercache:55000"
os.environ["http_proxy"] = "http://servercache:55000"
os.environ["https_proxy"] = "http://servercache:55000"


# construct the proxy url
import urllib.parse
uid = "LAN_ID"
password = "PASSWORD"
encoded_password = urllib.parse.quote(password)
proxy = f"http://{uid}:{encoded_password}@clientcache.prci.com:8080"
print(proxy)


# if need to set enviornment variables in python
import os
os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
