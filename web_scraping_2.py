from bs4 import BeautifulSoup
import re

with open("imdex.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")


#This get the option tag
tag = doc.find("option")
# This changes an attribute of a tag
tag['selected'] = 'false'

# This prints out the attribute of the tag
print(tag.attrs)

# This searches for multiple tags
tags = doc.find_all(["p", "div", "li"])

#This searches for the option tag with "undergraduate" as the value
tags = doc.find_all(["option"], text="Undergraduate")

# searching with classname
tags = doc.find_all(class_="btn_item") 

# searching with regular expressions
tags = doc.find_all(text=re.compile("\$.*"))

# limit number of results
tags = doc.find_all(text=re.compile("\$.*"), limit=1)


#changing the placeholder for input tags and  saving it in a new file
tags = doc.find_all("input", type="text")
for tag in tags:
    tag['placeholder'] = "I changed you!"

with open("changed.html", "w") as file:
    file.write(str(doc))