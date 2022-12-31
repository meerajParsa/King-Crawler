import inquirer
from validator_collection import validators, checkers
from mpscraper import MPScraper
# -------------------------------------------

target = None
url = None
message = "Please enter the web page address "

while url == None:
    getUrl = [inquirer.Text("url",message=message)]
    answers = inquirer.prompt(getUrl)
    if checkers.is_url(answers["url"]):
        url = answers["url"]
    else:
        message = "The URL entered is not correct (sample : http://google.com) "

while target == None:
    questions = [inquirer.List('Target',message="What do you want scraped ?",choices=['Links', 'Images'])]
    select = inquirer.prompt(questions)
    target = select["Target"]

init = MPScraper(url,target)

match target:
    case "Links":
        MPScraper.Links(init)
        pass
    case "Images":
        pass