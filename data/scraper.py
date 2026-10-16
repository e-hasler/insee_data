from bs4 import BeautifulSoup
import requests
import pandas as pd


def scrape_article(url):
    """
    Scrapes the article at the given URL and extracts tables with class 'divtab'.
    Returns a list of dictionaries containing the title and data of each table."""
    try:
        response = requests.get(url)
        #print(f"Response is {response.text[:100]}...")  # Print the first 100 characters of the response for debugging
        response.raise_for_status()  # Raise an error for HTTP errors
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    #print(f"Soup object created: {soup.prettify()[:100]}...")  # Print the first 100 characters of the prettified soup for debugging
    tables = soup.find_all('div', class_='divtab')
    #print(f"Tables is {tables}")  # Print table
    article_data = []

    for table in tables:
        title = table.find('th', class_='tittab').find(string=True, recursive=False).strip() if table.find('th', class_='tittab').find(string=True, recursive=False).strip() else "No Title"
        print(f"Title is {title}")  # Print title
        # Store table in article_data as dataframe
        df = pd.read_html(str(table))[0]
        data = {
            "title": title,
            "data": df.to_dict(orient='records')  # Convert DataFrame to list of dictionaries
        }
        article_data.append(data)

    print(f"Article data extracted: {article_data}")  # Print the extracted article data for debugging
    return article_data



# Test scraping for one article
url = "https://www.inegalites.fr/A-quels-niveaux-se-situent-les-seuils-de-pauvrete-en-France"
article_data = scrape_article(url)
"""
if article_data:
    for table in article_data:
        print(f"Title: {table['title']}")
        print(f"Data: {table['data']}\n")
else:
    print("No data found.")
"""

