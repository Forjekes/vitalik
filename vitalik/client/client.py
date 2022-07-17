import urllib.request


fp = urllib.request.urlopen("http://localhost:1234/")


print(fp.read().decode("utf8"))


fp.close()