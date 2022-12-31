from random import randint
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from bs4 import BeautifulSoup
import requests

class MPScraper:

    target = None
    url = None
    colorama_init()

    def __init__(self,url,target):
        self.url = url
        self.target = target
        
    def Links(self):
        links = []
        if self.url==None:
            print(f"{Fore.YELLOW}--- Please restart the program because the {Fore.RED}URL{Fore.YELLOW} was not entered ---{Style.RESET_ALL}")
        else:
            try:
                R = requests.get(self.url)
                soup = BeautifulSoup(R.content,"html.parser")
                for link in soup.find_all("a",href=True):
                    links.append(link['href']) if link['href']!=None else ''
                
                if(len(links)>0):
                    print(f'{Fore.GREEN}{links}{Style.RESET_ALL}')
                else:
                    print(f"{Fore.YELLOW}--- How interesting ! There were no links on this page :) ---{Style.RESET_ALL}")


            except ValueError:
                print(f"{Fore.YELLOW}--- There is an error connecting to the entered URL. Please try again after checking and fixing the error. {Fore.GREEN}(Tip: Your internet connection may have a problem){Fore.YELLOW} ---{Style.RESET_ALL}")
