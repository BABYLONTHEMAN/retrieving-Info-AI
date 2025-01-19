import requests
from bs4 import BeautifulSoup

def search_wikipedia(query, limit=5):
    """
    Searches Wikipedia using its OpenSearch API and returns a list of article URLs.
    :param query: The search term
    :param limit: How many search results to return
    :return: List of Wikipedia article URLs
    """
    # Wikipedia's OpenSearch endpoint:
    search_url = "https://en.wikipedia.org/w/api.php"

    # Parameters for the API request
    params = {
        'action': 'opensearch',
        'namespace': 0,
        'search': query,
        'limit': limit,
        'format': 'json'
    }

    # Make the request to the Wikipedia OpenSearch API
    response = requests.get(search_url, params=params)
    response.raise_for_status()

    # Parse the response. Format:
    # [
    #   queryString,
    #   [list_of_titles],
    #   [list_of_summaries],
    #   [list_of_links]
    # ]
    data = response.json()

    # The fourth element (index = 3) is the list of article URLs
    urls = data[3]
    return urls
x = input('wa chi dagarey? titly pageaka...   Given a list of Wikipedia URLs, scrape the page title, meta description,andd any paragraphs containing the specified keywords')
def scrape_wikipedia_pages(urls, keyword= x):
    for url in urls:
        try:
            print(f"Scraping URL: {url}")
            page_response = requests.get(url)
            page_response.raise_for_status()

            soup = BeautifulSoup(page_response.content, "html.parser")

            # Extract the page title
            title_tag = soup.find('title')
            if title_tag:
                print(f"Title: {title_tag.get_text(strip=True)}")

            # Extract meta description if available
            desc_tag = soup.find('meta', attrs={'name': 'description'})
            if desc_tag and desc_tag.get('content'):
                print(f"Description: {desc_tag['content']}")

            # Search paragraphs for the keyword
            found_keyword = False
            for p in soup.find_all('p'):
                if keyword.lower() in p.text.lower():
                    found_keyword = True
                    print("\n" + p.text.strip() + "\n")

            if not found_keyword:
                print(f"No paragraphs with the keyword '{keyword}' found.")
            print("-" * 60)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}:\n{e}\n{'-' * 60}")
d = input('wachi tr dagarey ? search_query =...')
keywordaka = input('keywordaka = ? kajwana kajwana ...')
if __name__ == "__main__":
    # Example: search for "Jack Bauer" and scrape the results
    search_query = d
    article_urls = search_wikipedia(search_query, limit=5)

    if article_urls:
        print(f"Found {len(article_urls)} articles for '{search_query}':\n")
        for idx, link in enumerate(article_urls, start=1):
            print(f"{idx}. {link}")
        print("\nStarting scrape...\n")

        scrape_wikipedia_pages(article_urls, keyword= keywordaka)
    else:
        print("No articles found.")