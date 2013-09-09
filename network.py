__author__ = 'Dyachkov'

import urllib
import urllib.request

class myURLOpener(urllib.request.FancyURLopener):
    # read an URL, with automatic HTTP authentication
    def setpasswd(self, user, passwd):
        self.__user = user
        self.__passwd = passwd

    def prompt_user_passwd(self, host, realm):
        return self.__user, self.__passwd

urlopener = myURLOpener()
urlopener.setpasswd("", "")

fp = urlopener.open("http://www.example.com")
print (fp.read())

print("Available proxies:")
print (urllib.request.getproxies())

#urllib.urlopen('http://www.python.org/', proxies={'http': 'http://:8080'})

#proxy_handler = urllib.request.ProxyHandler({'http': 'http://:8080'})
#opener = urllib.request.build_opener(proxy_handler)
#urllib.request.install_opener(opener)
#f = urllib.request.urlopen('http://www.python.org/')
