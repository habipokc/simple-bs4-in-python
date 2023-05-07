from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.contents[0].get("href")
    article_links.append(article_link)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)





















# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# #
# # for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)