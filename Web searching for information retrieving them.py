import requests
from bs4 import BeautifulSoup

query = "parrot bird"  # The search query
urls = ['https://www.parrots.org/encyclopedia', 'https://www.worldatlas.com/articles/parrot-facts-and-information.html', 'https://www.beautyofbirds.com/', 'https://www.birdlife.org/worldwide/news/flying-colours-10-unforgettable-parrot-facts', 'https://www.petmd.com/bird/care/evr_bd_parrot_facts', 'https://www.avianweb.com/parrots/', 'https://www.audubon.org/news/9-fascinating-facts-about-parrots', 'https://www.mnn.com/earth-matters/animals/stories/14-things-you-didnt-know-about-parrots', 'https://www.thesprucepets.com/parrots-and-other-pet-birds-390207', 'https://www.nationalgeographic.com/animals/birds/facts/parrot']

# Iterate over each URL and extract relevant information
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find('title').text.strip()
    print(f"Title: {title}\n")
    description = soup.find('meta', attrs={'name': 'description'})
    if description:
        print(f"Description: {description.get('content')}\n")
    for p in soup.find_all('p'):
        if 'parrot' in p.text.lower():
            print(p.text.strip())
            print("\n")
