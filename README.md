# webredirector

This script is a basic http redirector. I use this to sus out blind SSRF's 
 
https://stackoverflow.com/questions/2506932/how-do-i-redirect-a-request-to-a-different-url-in-python
 
sudo python3 redirector.py 800 http://127.0.0.1:8000/
 
https://realpython.com/python-http-server
 
python3 -m http.server 8000

testing
 
curl -v -L --insecure  http://127.0.0.1:800/dasfsdf
