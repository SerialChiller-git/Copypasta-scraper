import requests
from bs4 import BeautifulSoup
import random

pastas = []


def main():
    url = requests.get("https://www.vlr.gg/226976/funniest-copypastas")
    url2 = requests.get("https://emojicombos.com/copypasta")
    soup = BeautifulSoup(url.text, 'html.parser')
    soup2 = BeautifulSoup(url2.text, 'html.parser')

    # Print part of the HTML to inspect its structure
    #print(soup.prettify()[:1000])  # Print the first 1000 characters of the prettified HTML

    pastas = soup.find_all('div', class_ = 'post-body') + soup2.find_all('div', class_ = 'emojis')
    
    def generate():
        bruh = random.choice(pastas)
        print(bruh.text)


    generate()
    while(True):
        print("\n type 'kek' to fetch again ")
        kek = input()
        if(kek == "kek"):
            generate()
            print("\n")
        else:
            break


if __name__ == "__main__":
    main()
