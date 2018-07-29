import requests
from PIL import Image, ImageChops, ImageOps
from subprocess import check_output, PIPE

import sys


url_qr1 = "https://raw.githubusercontent.com/LASACTF/LASACTF-Problems/master/Problems/Forensics/pixels/QR1.png"
url_qr2 = "https://raw.githubusercontent.com/LASACTF/LASACTF-Problems/master/Problems/Forensics/pixels/QR2.png"

def download(url, save_name):
    resp = requests.get(url, stream = True)
    if (resp.status_code == 200):
        with open(save_name, "wb") as f:
            for chunk in resp:
                f.write(chunk)
    return resp.status_code

def stdprint(txt):
    sys.stdout.buffer.write(txt + b"\n")

def compare_merge_bw(a, b):
    diff = ImageChops.difference(a, b)
    new = diff.convert("L")
    new.paste(b, mask=diff)
    new = ImageOps.invert(new)
    return new

n1 = "QR1.png"
n2 = "QR2.png"
out = "result.png"

if (__name__ == "__main__"):
    if (download(url_qr1, n1) == 200) & (download(url_qr2, n2) == 200):
        
        img1 = Image.open(n1)
        img2 = Image.open(n2)
        
        compare_merge_bw(img1, img2).save(out, "PNG")
        
        img1.close()
        img2.close()

        stdprint(check_output(["zbarimg", out], stderr=PIPE).split()[-1])