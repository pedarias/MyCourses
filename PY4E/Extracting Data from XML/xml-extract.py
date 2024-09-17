import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    try:  # prompt the user for a url location and read it with urllib
        url = input("Enter location: ")
        xml = urllib.request.urlopen(url, context=ctx).read()
        break
    except:  # prevent invalid urls from crashing the program
        print("Invalid url. Try again.")
        continue

print("Retrieving", url)  # let the user know retrieval was successful
print(
    "Retrieved", len(xml), "characters"
)  # get the total number of characters in the file

# Parse the comments in the XML data
tree = ET.fromstring(xml)  # get the xml element tree
lst = tree.findall("comments/comment")  # place all comment tags in a list
print("Comment count:", len(lst))  # get the total number of comment tags

# Extract the counts and add them together
sum = 0  # initalize a sum variable
for item in lst:  # go through each comment item in the list
    count = item.find("count").text  # retrieve the count text
    sum += int(count)  # compute the sum of the extracted counts

print("The sum of all comments is:", sum)
