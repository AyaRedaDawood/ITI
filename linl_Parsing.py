import tldextract
import requests
from bs4 import BeautifulSoup
from bs4 import Comment

url=tldextract.extract('https://www.masrawy.com')
print ("Domain : " + url.domain)
print ("SubDomain : " + url.subdomain)

def extract_meta(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"xml")
    quotes = []
    for tag in soup.find_all(True):
            quotes.append("<" + tag.name + ">")

    tag = set(quotes)
    print("included Tags:-")
    for i in tag:
             print(i)

    print('included links :- ')
    for tag in soup.find_all("a"):
             print (tag.get('href'))

    print('included comments :- ')
    for comments in soup.findAll(text=lambda text:isinstance(text, Comment)):
             print("<!-- "+comments+" -->")



if __name__ == '__main__':
    _url = 'http://www.sourcebits.com/'
    extract_meta(_url)
