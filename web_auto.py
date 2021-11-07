import requests as rq
from bs4 import BeautifulSoup

baseURL = "https://realpython.github.io/fake-jobs/"
basepage = rq.get(baseURL)
soup = BeautifulSoup(basepage.content, "html.parser")
res = soup.find_all(class_ = "card-footer-item")
res2 = [r for r in res[1::2]] # every other element of the list (starting at the second element)

for r in res2:
    URL = r['href']
    filename = r['href'].split("/")[-1].replace(".html",".txt")
    page = rq.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    h1 = soup.find("h1").text
    h2 = soup.find("h2").text
    c = soup.find(class_ = "content").text
    f = open("jobs/"+filename,"w")
    f.write(h1)
    f.write(h2)
    f.write(c)
    f.close()