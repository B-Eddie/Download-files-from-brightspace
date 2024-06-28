from bs4 import BeautifulSoup
import webbrowser

# HTML code

file_path = "html.txt"  # Replace with the actual file path!!

with open(file_path, "r") as file:
    plain_text = file.read()

html = plain_text

soup = BeautifulSoup(html, "html.parser")

div_elements = soup.find_all('div', class_='d2l-htmlblock-untrusted')

google_doc = set()
google_slide = set()

for div in div_elements:
    d2l_block = div.find('d2l-html-block')
    if d2l_block and 'html' in d2l_block.attrs:
        embedded_html = d2l_block['html']

        embedded_soup = BeautifulSoup(embedded_html, "html.parser")

        a_elements = embedded_soup.find_all('a')
        for a in a_elements:
            link = a['href']
            if link[0] == "h" and "google" in link and "drive" not in link and "jamboard" not in link and "document" in link:
                link = link[:link.find('/edit')] + '/copy'
                google_doc.add(link)
            elif link[0] == "h" and "google" in link and "drive" not in link and "jamboard" not in link and "presentation" in link:
                google_slide.add(link)

docinput = ""
slideinput = ""
while docinput != "y" and docinput != "n" or slideinput != "y" and slideinput != "n":
    docinput = input("Open Google Docs links? (y/n): ")
    if docinput == "y":
        for i in google_doc:
            webbrowser.open(i)
    slideinput = input("Open Google Slides links? (y/n): ")
    if slideinput == "y":
        for slide in google_slide:
            webbrowser.open(slide)
