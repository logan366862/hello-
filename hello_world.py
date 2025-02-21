import requests
from bs4 import BeautifulSoup
html = requests.get("https://books.toscrape.com/").text
#html = BeautifulSoup(response,"html.parser")  #获得一个实例对象
soup=BeautifulSoup(html,"html.parser")
all_titles=soup.find_all("h3")
for title in all_titles:
    print(title.string)  #因为里面只有一个元素了，所以可以直接findAll一次，不然还需要使用一次findAll
