# simple-bs4-in-python
This Python code uses the BeautifulSoup and requests libraries to fetch data from "https://news.ycombinator.com/".

The code retrieves the article titles, links, and upvotes from the Hacker News website. Firstly, it uses the requests.get() method to fetch the source code of the web page. Then, the BeautifulSoup library is used to parse and convert this source code into HTML.

The article titles (article_texts), article links (article_links), and article upvotes (article_upvotes) are extracted and added to lists. This information is obtained using BeautifulSoup methods like find_all() and getText().

Finally, the obtained title, link, and upvote information is printed to the screen.

Make sure you have installed the BeautifulSoup and requests libraries for the code to run properly.
