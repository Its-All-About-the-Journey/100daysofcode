from bs4 import BeautifulSoup


if __name__ == "__main__":
    with open("website.html") as file_in:
        content = file_in.read()

    soup = BeautifulSoup(content, "html.parser")

    print(soup.title)
    print(soup.title.name)
    print(soup.title.string)

    print(soup.prettify())

    print(soup.p)

    # Finding all by tag, class, and/or id
    tags = soup.find_all(name="a")

    for tag in tags:
        print(tag.getText())
        print(tag.get("href"))

    heading = soup.find(name="h1", id="name")
    print(heading)

    section_heading = soup.find(name="h3", class_="heading")
    print(section_heading)

    # Selecting by tags, class, and/or id
    # - used for more specific selection
    company_url = soup.select_one(selector="p a")
    print(company_url)

    headings = soup.select(".heading")
    print(headings)
