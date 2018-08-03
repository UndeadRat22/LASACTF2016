#!/usr/bin/env python3
import requests
import zipfile
from re import findall as regex

main_url = "https://raw.githubusercontent.com/LASACTF/LASACTF-Problems/master/Problems/Forensics/sounds-strange/"
zip_filename = "sounds_strange.zip"
encrypted_name = "sounds_strange.aiff"
zip_url = main_url + zip_filename


def download(url, save_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_name, "wb") as file:
            file.write(response.content)
    return response.status_code

def extract(filename):
    with zipfile.ZipFile(filename, "r") as zip_ref:
        if zipfile:
            zip_ref.extractall()

def byte_subtract(byte, value):
    for _ in range(0, value):
        byte = byte - 1
        if (byte < 0):
            byte = 0xFF
    return byte

def decrypt(filename):
    with open(filename, "rb") as file:
        text = file.read()
        out = ""
        for byte in text:
            if (byte < 0x80):
                continue
            out += chr(byte - 0x80)
    return out

def get_flag():
    if download(zip_url, zip_filename) != 200:
        print("failed to download file:{}\nurl = {}".format(zip_filename, zip_url))
        return None
    
    extract(zip_filename)
    string = decrypt(encrypted_name)
    return (regex(r"lasactf{(.*)}", string)[0])

if __name__ == "__main__":
    print(get_flag())