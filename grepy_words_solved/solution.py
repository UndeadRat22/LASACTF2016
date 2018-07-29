import requests

#the file had to be found by using grep as the name suggests

url = "https://raw.githubusercontent.com/LASACTF/LASACTF-Problems/master/Problems/Miscellaneous/grep-quest/grepy-words/potato.txt"

if (__name__ == "__main__"):
    resp = requests.get(url)
    if (resp.status_code == 200):
        print(resp.content)