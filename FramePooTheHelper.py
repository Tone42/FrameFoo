import requests
from bs4 import BeautifulSoup

# Define the list of URLs to extract links from
urls = [
    "https://www.lenscrafters.com/lc-us/brands/armani-exchange",
    "https://www.lenscrafters.com/lc-us/brands/arnette",
    "https://www.lenscrafters.com/lc-us/brands/brooks-brothers",
    "https://www.lenscrafters.com/lc-us/brands/burberry",
    "https://www.lenscrafters.com/lc-us/brands/chaps",
    "https://www.lenscrafters.com/lc-us/brands/coach",
    "https://www.lenscrafters.com/lc-us/brands/costa-del-mar",
    "https://www.lenscrafters.com/lc-us/brands/tiffany",
    "https://www.lenscrafters.com/lc-us/brands/ray-ban"
]

# Define the headers to send with the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Define an empty list to store all the links
all_links = []

# Loop through each URL and extract the links
for url in urls:
    print("Sending request to", url)
    try:
        # Send a GET request to the URL with the headers and store the HTML response
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        continue

    print("Received response from", url)

    # Parse the HTML response with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all links in the HTML and extract the href attribute
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.startswith("https"):
            links.append(href)

    # Add the links to the list of all links
    all_links.extend(links)

# Save the list of links to a text file
with open("all_links.txt", "w") as f:
    for link in all_links:
        f.write(link + "\n")

print("Saved links to all_links.txt")
