import requests
import re
from subprocess import check_output as cmd

fileurl = "https://raw.githubusercontent.com/LASACTF/LASACTF-Problems/master/Problems/Reverse%20Engineering/easy/easy.exe"
filename = "easy.exe"

def download(url):
    resp = requests.get(fileurl)
    if (resp.status_code == 200):
        return resp.content

if (__name__ == "__main__"):
    filedata = download(fileurl)
    if (not filedata):
        exit(-1)
    with open(filename, "wb") as file:
        file.write(filedata)
    
    try:
        result = cmd(["strings", filename])
    except Exception as e:
        print("could not parse the file {} using strings!".format(filename))
        print(e)
    
    if (not result):
        exit(-1)

    flags = re.findall(r"lasactf{(.*)}", str(result))
    print(flags[0][:17])