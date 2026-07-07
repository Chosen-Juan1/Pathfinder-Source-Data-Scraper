from bs4 import BeautifulSoup
import requests

def getLinks(selector:str, beautyLinks:BeautifulSoup, baseLink:str):
    links = beautyLinks.select(selector)
    listOfLinks = []
    for link in links:
        # print(str(link))
        link = str(link).split("\"")
        for segments in link:
            if "http" in segments:
                if(segments == baseLink):
                    continue
                listOfLinks.append(segments)
                #  print(segments)
    # print(listOfLinks)
    return listOfLinks
if __name__ == "__main__":
    baseLink = "https://www.d20pfsrd.com/magic/all-spells"
    response = requests.get(baseLink)
    selector = "[href*='https://www.d20pfsrd.com/magic/all-spells/']"
    beautyLink = BeautifulSoup(response.text,'html.parser')

    listOfLinks = getLinks(selector, beautyLink, baseLink)
    print(listOfLinks)