import os
import requests
from urllib.parse import urlparse

def download_image(url, filename):
    # Create directory if it doesn't exist
    directory = "FramePhotoFoo"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the URL to get the file extension
    file_extension = os.path.splitext(urlparse(url).path)[1]

    # Save the image to the directory
    filepath = os.path.join(directory, f"{filename}{file_extension}")
    with open(filepath, 'wb') as f:
        f.write(response.content)
