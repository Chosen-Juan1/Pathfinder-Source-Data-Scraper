from Utilities.getSpellDetailsD20PFSRD import getSpellDetails
from Utilities.getGeneralSpellLinks import getLinks
from bs4 import BeautifulSoup
import requests

def tabulateSpells(baseLink, selector):
    response = requests.get(baseLink)
    beautyLink = BeautifulSoup(response.text,'html.parser')
    spellTable = {"NAME" : [], "LEARNED BY" : [], "CASTING" : [], "EFFECT" : [], "DESCRIPTION" : [], "LINK" : []}
    # baseLink = "https://www.d20pfsrd.com/magic/all-spells/"
    listOfLinks = getLinks(selector, beautyLink, baseLink)
    for link in listOfLinks:
        spellHTMLPage = requests.get(link)
        prettyPage = BeautifulSoup(spellHTMLPage.text,'html.parser')
        details = getSpellDetails(prettyPage, link)
        # print()
        try:
            spellTable["NAME"].append(details["NAME"])
        except:
            spellTable["NAME"].append(None)
        # spellTable["LEARNED BY"].append(details["LEARNED BY"])
        try:
            spellTable["CASTING"].append(details["CASTING"])
        except:
            spellTable["CASTING"].append(None)
        try:
            spellTable["EFFECT"].append(details["EFFECT"])
        except:
            spellTable["EFFECT"].append(None)
        try:
            spellTable["DESCRIPTION"].append(details["DESCRIPTION"])
        except:
            spellTable["DESCRIPTION"].append(None)
        spellTable["LINK"].append(details["LINK"])
    return spellTable


if __name__ == "__main__":

    baseLink = "https://www.d20pfsrd.com/magic/all-spells/"
    selector = f"[href*='{baseLink}']"
    tabulateSpells(baseLink, selector)
    print("DONE")
