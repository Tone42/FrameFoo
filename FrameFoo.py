import requests
from bs4 import BeautifulSoup
import re
import sqlite3

# Make a request to the webpage with additional headers
url = 'https://www.lenscrafters.com/lc-us/ray-ban/8053672727708'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.9'
}
response = requests.get(url, headers=headers)

# Parse the HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Find the element using XPath
element = soup.find('span', {'class': 'printMillimeters'})

# Extract the text from the element
measurements = element.text.strip()

# Find the image URL and title
title_elem = soup.find('meta', {'property': 'og:title'})
frame_name = title_elem['content'] if title_elem else ''

# Find the URL
url_pattern = r'https://assets.lenscrafters.com/is/image/LensCrafters/[^"]+'
url_matches = re.findall(url_pattern, str(soup))
photo_link = url_matches[0] if url_matches else ''

# Store the data in a database
conn = sqlite3.connect('framinfo.db')
c = conn.cursor()

# Create the table if it does not exist
c.execute('CREATE TABLE IF NOT EXISTS data (frame_name text, measurements text, photo_link text)')

# Insert the data into the table
c.execute('INSERT INTO data (frame_name, measurements, photo_link) VALUES (?, ?, ?)', (frame_name, measurements, photo_link))
conn.commit()

conn.close()
