import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
         pass
    except requests.exceptions.InvalidURL:
        pass
    
targer_url = input("Enter a URL: ")

with open("wordlist.txt") as wordlist_file:
    for line in wordlist_file:
        line = line.strip("\n")
        url = line + "." +  target_url
        response = request(url)
        if response:
            print("[+] discovered subdomain --> " + url)
