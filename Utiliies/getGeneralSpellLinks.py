from bs4 import BeautifulSoup

def getLinks(selector, beautyLinks):
    links = beautyLinks.select(selector)
    listOfLinks = []
    for link in links:
        # print(str(link))
        link = str(link).split("\"")
        for segments in link:
            if "http" in segments:
                listOfLinks.append(segments)
                #  print(segments)
    listOfLinks