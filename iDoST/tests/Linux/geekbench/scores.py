# importing the libraries
from bs4 import BeautifulSoup
import requests
import sys

def GetScore(url):
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, features="html.parser")
    scores = {
        'Single-Core Score': None,
        'Multi-Core Score': None,
    }

    for key in scores:
        scores[key] = soup.find("div", attrs={"class": "note"}, text = key).previous_element.previous_element
    return scores

if __name__ == "__main__":
    GetGeekBenchScore(sys.argv[1])
