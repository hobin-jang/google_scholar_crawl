import urllib.request
from bs4 import BeautifulSoup

url = "https://scholar.google.com/scholar?start=0&q=chameleon+hash+blockchain&hl=ko&as_sdt=0,5"

header = {"User-Agent": "Mozilla/5.0"}

page = urllib.request.Request(url, headers=header)
html = urllib.request.urlopen(page)
soup = BeautifulSoup(html, 'html.parser')

info = soup.select('div.gs_ri')
for inf in info:
    title = inf.find('h3','gs_rt')
    num = inf.find('div','gs_fl')

    print(title.get_text())
    print()
    print(num.get_text())

    test = num.get_text()
    res = ""
    for idx in range(len(test)):
        if test[idx] == '회':
            last = idx
            start = idx 
            while True:
                if test[idx] == ' ':
                    start = idx + 1 
                    break
                idx -= 1 
            print(test[start:last]) 
            
    