from googleapiclient.discovery import build
import re
import requests
from bs4 import BeautifulSoup

my_api_key = "YOUR_API_KEY"
my_cse_id = "YOUR_CUSTOM_SEARCH_ENGINE_ID"
QUERY = "YOUR_SEARCH_QUERY"

def contentSearch(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text.strip())
    if soup.find(text=re.compile(line)):
        return True
    else:
        return False

def textsearch(url):
    global line
    file = [] #Enter the key words that you are looking for in the websites note that the words are case sensitive
    for line in file:
        print(line)
        if(contentSearch(url)):
            print(url) #Print the Url
            break
        else:
            pass

def google_search(search_term, api_key, cse_id, **kwargs):
      service = build("customsearch", "v1", developerKey=api_key)
      res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
      return res['items']

results= google_search(QUERY,my_api_key,my_cse_id,num=10) 

for result in results:
    textsearch(result["link"])