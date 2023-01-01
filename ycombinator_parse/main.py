from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_link = article_tag.get("href")
    
article_upvotes = soup.find_all(name="span", class_="score").getText()

print(article_text)
print(article_link)
print(article_upvote)
