import requests
from bs4 import BeautifulSoup
#نەوتی کوردستان چی دەبێت؟    نەوت

query = "نەوت"  # The search query
urls = ['https://www.parrots.org/encyclopedia', 'https://www.rudaw.net/sorani']

# Iterate over each URL and extract relevant information
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find('ن').text.strip()
    print(f"Title: {title}\n")
    description = soup.find('meta', attrs={'name': 'description'})
    if description:
        print(f"Description: {description.get('content')}\n")
    for p in soup.find_all('p'):
        if 'ن' in p.text.lower():
            print(p.text.strip())
            print("\n")
