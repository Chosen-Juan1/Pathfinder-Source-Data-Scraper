from bs4 import BeautifulSoup
import requests

def getLinks(selector:str, beautyLinks:BeautifulSoup):
    links = beautyLinks.select(selector)
    listOfLinks = []
    for link in links:
        # print(str(link))
        link = str(link).split("\"")
        for segments in link:
            if "http" in segments:
                listOfLinks.append(segments)
                #  print(segments)
    # print(listOfLinks)
    return listOfLinks
if __name__ == "__main__":
    response = requests.get("https://www.d20pfsrd.com/magic/all-spells")
    selector = "[href*='https://www.d20pfsrd.com/magic/all-spells/']"
    beautyLink = BeautifulSoup(response.text,'html.parser')

    listOfLinks = getLinks(selector, beautyLink)
    print(listOfLinks)