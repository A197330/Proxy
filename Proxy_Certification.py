# Set the path for the SSL certificate and proxy settings  

# Before run the following code, check the exact name of certificate in your env by run the following in terminal
$ ls /etc/ssl/certs/

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
