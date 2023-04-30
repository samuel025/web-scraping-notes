from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/xfx-radeon-rx-6700-xt-rx-67xtyjfdv/p/N82E16814150852?Item=N82E16814150852&cm_sp=Homepage_SS-_-P0_14-150-852-_-04302023&quicklink=true"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)