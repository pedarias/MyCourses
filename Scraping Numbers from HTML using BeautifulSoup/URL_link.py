from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen("http://py4e-data.dr-chuck.net/comments_1841323.html").read()
doc = BeautifulSoup(html, "html.parser")
tags = doc("span")
sum = 0
for tag in tags:
    sum = sum + int(tag.contents[0])
print(sum)

# to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers
