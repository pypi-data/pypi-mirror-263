import requests as r
import socket as s

class DotDict:
    def __init__(self, dictionary):
        self.__dict__.update(dictionary)

    def __getattr__(self, item):
        return self.__dict__.get(item)

    def __setattr__(self, key, value):
        self.__dict__[key] = value


# You can add more functions or classes here if needed


class WebTools:
    def __init__(self):
        self.StatusCodes = self.StatusCodes()

        self.DirsChecked = []

        self.RequestHeaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }

        self.URLHTTP = str
        self.URLHTTPS = str

    class StatusCodes:
        def __init__(self):
            self.Informational = [100, 101, 102, 103]
            self.Success = [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]
            self.Redirection = [300, 301, 302, 303, 304, 305, 306, 307, 308]
            self.ClientError = [400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417,
                                418, 421, 422, 423, 424, 425, 426, 428, 429, 431, 451]
            self.ServerError = [500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]


    def FetchTLDs(self):

        self.TLDSs = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"
        response = r.get(self.TLDSs, headers=self.RequestHeaders)
        response.raise_for_status()

        # The file uses line breaks for each TLD, and we filter out comments which start with '#'
        self.TLDS = [line.strip().lower() for line in response.text.splitlines() if not line.startswith('#')]

    def ValidTLD(self, URL=None):

        self.FetchTLDs()

        TLDSValid = False

        if URL.endswith("/"):
            URL = URL[:-1]

        URLTLDS = URL[URL.rindex('.')+1:]

        for i in self.TLDS:
            if URLTLDS == i:
                TLDSValid = True
                break

        if TLDSValid is False:
            return False
        else:
            return True

    def RefactorHTTP(self, URL=None):

        if URL.endswith("/"):  # Checks if the URL ends with a forward slash
            URL = URL[:-1]  # Removes the forward slash from the URL

        for i in "https://", "http://":
            if URL.startswith(i):
                if i == "https://":
                    self.URLHTTP = URL.replace("https://", "http://")

                if i == "http//":
                    self.URLHTTP = URL
                break
            else:
                self.URLHTTP = f"http://{URL}"

        return self.URLHTTP

    def RefactorHTTPS(self, URL=None):  # defines the refactor function and passes the URL variable as a parameter

        if URL.endswith("/"):  # Checks if the URL ends with a forward slash
            URL = URL[:-1]  # Removes the forward slash from the URL

        for i in "https://", "http://":
            if URL.startswith(i):
                if i == "https://":
                    self.URLHTTPS = URL

                if i == "http//":
                    self.URLHTTPS = URL.replace("http://", "https://")

                break
            else:
                self.URLHTTPS = f"https://{URL}"

        return self.URLHTTPS

    def HTTPcheck(self, URL=None):

        self.RefactorHTTP(URL=URL)

        URL = self.URLHTTP

        GetReqStatus = r.get(url=URL, headers=self.RequestHeaders)

        if GetReqStatus.status_code in self.PositiveStatusCodes:
            return True
        else:
            return False

    def HTTPScheck(self, URL=None):

        self.RefactorHTTPS(URL=URL)

        URL = self.URLHTTPS

        GetReqStatus = r.get(url=URL, headers=self.RequestHeaders)

        if GetReqStatus.status_code == 200:
            return True
        else:
            return False



"""

===EXAMPLES===


Command:
    WebTools.RefactorHTTPS(URL='www.google.com') # Refactors URL by adding https

Example:

    URLHTTPS = WebTools.HTTPSRefactor(URL='www.google.com')

    print(f"URL HTTPS: {URLHTTPS}")


Command:
    WebTools.RefactorHTTP(URL='www.google.com') # Refactors URL by adding http

Example:
    URLHTTP = WebTools.RefactorHTTP(URL='www.google.com') # Refactors URL by adding http

    print(f"URL HTTP: {URLHTTP}")
    

Command: 
    WebTools.HTTPcheck(URL='www.google.com') # Checks if URL using http is valid  
    
Example:
    if WebTools.HTTPcheck(URL='www.google.com') == True:
        print('HTTP is Valid')


Command:
    WebTools.HTTPScheck(URL='www.google.com') # Checks if URL using https is valid

Example:  
    if WebTools.HTTPScheck(URL='www.google.com') == True:
        print('HTTPS is Valid')

Command:
    WebTools.ValidTLDS(URL='www.google.com') # Checks if the URLs TLDS is valid 


Example:
    if WebTools.ValidTLDS(URL='www.google.com') == False: 
        print('TLDS is invalid')
    else:
        print('TLDS is valid')

Command:
    WebTools.RequestHeaders


Example:
    r = requests.get(URLHTTPS, headers=WebTools.RequestHeaders)
    print(r.status_code)
    
    
Command:
    WebTools.PositiveStatusCodes

Example:
    if r.status_code in WebTools.PositiveStatusCodes:
        print(f"{r.status_code} is in PositiveStatusCodes list")
    
    
    
    
    
    
    
from PyPiFiles import WebTools
import requests


WebTools = WebTools.WebTools()


if WebTools.ValidTLD(URL='www.google.cdasasdom') == False:
    print('TLDS is invalid')
else:
    print('TLDS is valid')


if WebTools.HTTPScheck(URL='www.google.com') == True:
    print('HTTPS is Valid')


if WebTools.HTTPcheck(URL='www.google.com') == True:
        print('HTTP is Valid')


URLHTTPS = WebTools.RefactorHTTPS(URL='www.google.com')
URLHTTP = WebTools.RefactorHTTP(URL='www.google.com')

print(f"URL HTTPS: {URLHTTPS}")
print(f"URL HTTP: {URLHTTP}")


r = requests.get(URLHTTPS, headers=WebTools.RequestHeaders)
if r.status_code in WebTools.PositiveStatusCodes:
    print(f"{r.status_code} is in PositiveStatusCodes list")
    
    
    
    
    

"""