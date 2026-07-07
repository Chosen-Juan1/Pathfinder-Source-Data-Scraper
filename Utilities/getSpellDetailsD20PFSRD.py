from bs4 import BeautifulSoup

def getSpellDetails(beautySoupedPage, link):

    title = beautySoupedPage.find("h1").get_text()
    res = beautySoupedPage.find_all("p")
    # print(title.rfind(" – d20PFSRD"))
    # if(' – d20PFSRD' in title):
    #     print("check")
    #     removeIndex = title.rfind(" – d20PFSRD")
    #     title = title[:removeIndex]
    res = beautySoupedPage.find_all("p")
    listRes = list(res)
    classing = ["CASTING", "EFFECT", "DESCRIPTION"]
    sections = {}
    sections["NAME"] = title
    inputNow = False
    section = "LEARNED BY"
    spaceFlag = True #can't figure out how to stop the first bit from appearing
    for tags in range(0,len(listRes)):
        # print(listRes[tags].get_text())
        if(tags == 1): #this is to catch the info about who learns the spell, which is not under a section like the other info
            sections["LEARNED BY"] = listRes[tags].get_text()
            continue
        if(listRes[tags].get_text() == "Join Our Discord!" or "Editor’s Note" in listRes[tags].get_text() or "Note:" in listRes[tags].get_text()):
            break
        # if("Editor’s Note" in listRes[tags].get_text()):
        #     continue
        # print("\n")
        if(listRes[tags].get_text() in classing and inputNow == True):
            inputNow = False
        if(inputNow):
            if section in sections:
                sections[section] += " " + listRes[tags].get_text()
            else:
                if(spaceFlag):
                    sections[section] = listRes[tags].get_text() + ". "
                    spaceFlag = False
                else:
                    sections[section] = listRes[tags].get_text()
        if(listRes[tags].get_text() == "CASTING"):
            section = "CASTING"
            inputNow = True
        elif(listRes[tags].get_text() == "EFFECT"):
            section = "EFFECT"
            inputNow = True
        elif(listRes[tags].get_text() == "DESCRIPTION"):
            section = "DESCRIPTION"
            inputNow = True
    sections["LINK"] = link
    print("\n", sections)
    return sections

if __name__ == "__main__":
    import requests
    # link = "https://www.d20pfsrd.com/magic/all-spells/m/magic-missile/"
    link = " https://www.d20pfsrd.com/magic/3rd-party-spells/4-winds-fantasy-gaming-3rd-party-spells/analyze-fertility/"

    result = requests.get(link)
    result = BeautifulSoup(result.text,'html.parser')

    # listOfLinks = getLinks(selector, beautyLink)
    # print(listOfLinks)
    print(getSpellDetails(result, link))