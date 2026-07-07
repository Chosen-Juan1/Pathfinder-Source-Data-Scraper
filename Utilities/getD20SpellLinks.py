def getSpellLinks(listOfRawLinks):
    listOfLinks = []
    for link in listOfRawLinks:
            # print(str(link))
        link = str(link).split("\"")
        for segments in link:
            if "http" in segments:
                listOfLinks.append(segments)
                #  print(segments)
    return listOfLinks