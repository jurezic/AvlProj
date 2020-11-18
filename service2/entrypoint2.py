import requests
import urllib.request as request
import jrpc
import sys
"""
SERVICE1_URL = "http://service.example.com:8080"

message = requests.get(sys.stdin.readline()).text
data = ["md5", message]

print(requests.post(SERVICE1_URL, data="\n".join(data)))
"""
r = request.urlopen('https://www.python.org')
r = r.read()
print(r)

def downloadWebsite(url):
    try:
        content = request.urlopen(url)
        content = content.read()
        return content
    except:
        print("The given url is not valid!")

if __name__ == "__main__":
    url = input("Please enter the website url -> ")
    content = downloadWebsite(url)
    print("Sending the content to the hashing server...")
    hashing_server = jrpc.service.SocketProxy(50001)
    print(hashing_server.echo(content))