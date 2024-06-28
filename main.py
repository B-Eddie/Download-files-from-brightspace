from bs4 import BeautifulSoup
import webbrowser

# HTML code

file_path = "html.txt"  # Replace with the actual file path

with open(file_path, "r") as file:
    plain_text = file.read()


html = plain_text


soup = BeautifulSoup(html, "html.parser")

# Find all <div> elements with the class "d2l-htmlblock-untrusted"
div_elements = soup.find_all('div', class_='d2l-htmlblock-untrusted')

google_doc = []
google_slide = []
# Iterate through each <div> element
for div in div_elements:
    # Extract the content of the html attribute
    d2l_block = div.find('d2l-html-block')
    if d2l_block and 'html' in d2l_block.attrs:
        embedded_html = d2l_block['html']
        
        # Convert the embedded HTML from HTML entities back to standard HTML
        embedded_soup = BeautifulSoup(embedded_html, "html.parser")
        
        # Find all <a> elements in the embedded HTML and print their href attributes
        
        a_elements = embedded_soup.find_all('a')
        for a in a_elements:
            link = a['href']
            if link[0] == "h" and "google" in link and "drive" not in link and "jamboard" not in link and "document" in link:
                link = link[:link.find('/edit')] + '/copy'
                google_doc.append(link)
            elif link[0] == "h" and "google" in link and "drive" not in link and "jamboard" not in link and "presentation" in link:
                google_slide.append(link)
for i in google_doc:
    webbrowser.open(i)
for slide in google_slide:
    webbrowser.open(slide)