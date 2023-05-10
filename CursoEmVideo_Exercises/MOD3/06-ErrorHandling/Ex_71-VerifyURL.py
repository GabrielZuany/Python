#Verify if a URL is acessible.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/watch?v=oIwZp65Nxbk')
except:
    print('Error!')
else:
    print('OK!')
    print(site.read())