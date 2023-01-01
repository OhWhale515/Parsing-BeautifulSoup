from bs4 import BeautifulSoup

with open("website.html", "r", encoding="utf-8", errors="ignore") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
# print(soup.title.name)
# print(soup.prettify())
# print(soup)