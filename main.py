




import requests
from bs4 import BeautifulSoup
from html_text import extract_text
url = "https://www.naver.com/blog/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
visible_text = extract_text(str(soup))
print(visible_text)





