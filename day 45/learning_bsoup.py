from bs4 import BeautifulSoup
# import lxml

with open("Python-100-days-of-code/day 45/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)

# print(soup.prettify())  Get hold of All HTML code

# print(soup.p)  Get hold of the 1st element <p>

all_anchor_tags = soup.find_all("a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

company_url = soup.select_one(selector="p a")
print(company_url)





