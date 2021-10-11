from urllib import request
try:
    site = request.urlopen('http://www.pudim.com.br')
except:
    print('Pudim NÃO está acessível!')
else:
    print('Pudim ESTÁ acessível!')
    #print(site.read()) #tras o codigo do site
