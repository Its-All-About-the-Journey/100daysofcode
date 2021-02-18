from bs4 import BeautifulSoup
import requests

URL = "https://news.ycombinator.com"

if __name__ == "__main__":
    content = requests.get(URL)
    content.raise_for_status()

    soup = BeautifulSoup(content.text, "html.parser")

    article_tags = soup.find_all(name="a", class_="storylink")
    article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

    article_texts = list()
    article_links = list()

    for article_tag in article_tags:
        text = article_tag.getText()
        article_texts.append(text)

        link = article_tag.get("href")
        article_links.append(link)

    print(article_texts, end="\n\n")
    print(article_links, end="\n\n")
    print(article_upvotes, end="\n\n")

    largest_index = article_upvotes.index(max(article_upvotes))

    print(article_texts[largest_index])
    print(article_links[largest_index])
    print(article_upvotes[largest_index])