import scraper
import database
from photodownloader import download_image
import re

# Define a list of URLs to scrape
urls = [
    'https://www.lenscrafters.com/lc-us/michael-kors/725125000321',
'https://www.lenscrafters.com/lc-us/michael-kors/725125000406',
'https://www.lenscrafters.com/lc-us/michael-kors/725125388207',
'https://www.lenscrafters.com/lc-us/michael-kors/725125388207',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672767872',
'https://www.lenscrafters.com/lc-us/ray-ban/8056597664080',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672767940',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672767940',
'https://www.lenscrafters.com/lc-us/prada/8056597438162',
'https://www.lenscrafters.com/lc-us/prada/8056597438209',
'https://www.lenscrafters.com/lc-us/prada/8056597438209',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672770421',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672770438',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672977332',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672770445',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672770445',
'https://www.lenscrafters.com/lc-us/versace/8056597725163',
'https://www.lenscrafters.com/lc-us/versace/8056597725583',
'https://www.lenscrafters.com/lc-us/versace/8056597725149',
'https://www.lenscrafters.com/lc-us/versace/8056597725149',
'https://www.lenscrafters.com/lc-us/oakley/888392607195',
'https://www.lenscrafters.com/lc-us/oakley/888392575104',
'https://www.lenscrafters.com/lc-us/oakley/888392575128',
'https://www.lenscrafters.com/lc-us/oakley/888392575142',
'https://www.lenscrafters.com/lc-us/oakley/888392575142',
'https://www.lenscrafters.com/lc-us/ray-ban/7895653267657',
'https://www.lenscrafters.com/lc-us/ray-ban/7895653267657',
'https://www.lenscrafters.com/lc-us/ray-ban/805289439899',
'https://www.lenscrafters.com/lc-us/ray-ban/805289439936',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672416107',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672416107',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672808469',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672808476',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672808476',
'https://www.lenscrafters.com/lc-us/michael-kors/725125032278',
'https://www.lenscrafters.com/lc-us/michael-kors/725125032223',
'https://www.lenscrafters.com/lc-us/michael-kors/725125032223',
'https://www.lenscrafters.com/lc-us/prada/8056597747745',
'https://www.lenscrafters.com/lc-us/prada/8056597747745',
'https://www.lenscrafters.com/lc-us/ray-ban/713132838167',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672195781',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672195736',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672832839',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672832815',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672832778',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672832778',
'https://www.lenscrafters.com/lc-us/versace/8056597726429',
'https://www.lenscrafters.com/lc-us/versace/8056597726436',
'https://www.lenscrafters.com/lc-us/versace/8056597726443',
'https://www.lenscrafters.com/lc-us/versace/8056597726443',
'https://www.lenscrafters.com/lc-us/gucci/889652048123',
'https://www.lenscrafters.com/lc-us/gucci/889652048123',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672991338',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672991352',
'https://www.lenscrafters.com/lc-us/ray-ban/8053672991352',
'https://www.lenscrafters.com/lc-us/oakley/888392399823',
'https://www.lenscrafters.com/lc-us/oakley/888392399847',
'https://www.lenscrafters.com/lc-us/oakley/888392577863',
'https://www.lenscrafters.com/lc-us/oakley/888392577863',
'https://www.lenscrafters.com/lc-us/prada/8056597418478',
'https://www.lenscrafters.com/lc-us/prada/8056597435581',
'https://www.lenscrafters.com/lc-us/prada/8056597452465',
'https://www.lenscrafters.com/lc-us/prada/8056597452465',
'https://www.lenscrafters.com/lc-us/versace/8056597384520',
'https://www.lenscrafters.com/lc-us/versace/8056597384551',
'https://www.lenscrafters.com/lc-us/versace/8056597384551',
'https://www.lenscrafters.com/lc-us/prada/8056597626330',
'https://www.lenscrafters.com/lc-us/prada/8056597626309',
'https://www.lenscrafters.com/lc-us/prada/8056597626347',
'https://www.lenscrafters.com/lc-us/prada/8056597626170',
'https://www.lenscrafters.com/lc-us/prada/8056597626170',
'https://www.lenscrafters.com/lc-us/versace/8056597049818',
'https://www.lenscrafters.com/lc-us/versace/8056597049818',
'https://www.lenscrafters.com/lc-us/tory-burch/725125996204',
'https://www.lenscrafters.com/lc-us/tory-burch/725125996235',
'https://www.lenscrafters.com/lc-us/tory-burch/725125364072',
'https://www.lenscrafters.com/lc-us/tory-burch/725125364072',
'https://www.lenscrafters.com/lc-us/ray-ban/805289602057',
'https://www.lenscrafters.com/lc-us/ray-ban/805289114567',
'https://www.lenscrafters.com/lc-us/ray-ban/805289115694',
'https://www.lenscrafters.com/lc-us/ray-ban/805289115694',
'https://www.lenscrafters.com/lc-us/oakley/888392133205',
'https://www.lenscrafters.com/lc-us/oakley/888392078360',
'https://www.lenscrafters.com/lc-us/oakley/888392133212',
'https://www.lenscrafters.com/lc-us/oakley/888392172389',
'https://www.lenscrafters.com/lc-us/oakley/888392405074',
'https://www.lenscrafters.com/lc-us/oakley/888392405203',
'https://www.lenscrafters.com/lc-us/oakley/888392577832',
'https://www.lenscrafters.com/lc-us/oakley/888392577832'
]

# Loop over the URLs
for url in urls:
    # Scrape the data
    frame_name, measurements, photo_link = scraper.scrape(url)

    # Save the data to the database
    database.save_data(frame_name, measurements, photo_link)

    # Download the image and save it to the directory
    filename = re.sub('[^\w\-_\. ]', '-', frame_name)
    download_image(photo_link, filename)