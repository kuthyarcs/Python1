import requests
import bs4

url = 'https://sangamone.com'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
 
# Extracting data, e.g., all the links on the page
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
