import bs4
import requests
import os
from sys import *

def LinksDisplay(URL):
    res = requests.get(URL)
    print(type(res))

    soup = bs4.BeautifulSoup(res.text,'lxml')
    print(type(soup))

    links = soup.find_all('a',href = True)

    return links

def main():
    print("Application name : ",argv[0])

    if (len(argv) == 2):
        if(argv[1] == '-h') or (argv[1] == '-H'):
            print("The script is used to fetch links from wikipedia file")
            exit()

        if(argv[1] == '-u') or (argv[1] == '-U'):
            print("usage : ApplicationName")
            exit()

    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    arr = LinksDisplay(url)
    print("Links are : ")

    for element in arr:
        if '#' not in element['href']:
            print(element['href'])

if __name__ == "__main__":
    main()