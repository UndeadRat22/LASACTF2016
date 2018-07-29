import requests
from PIL import Image

img_url = "https://raw.githubusercontent.com/LASACTF/LASACTF-Problems/master/Problems/Forensics/r3ndom-eye/eyeofthetiger.png"
offset = 0x1FA87E
src_name = "eyeofthetiger.png"
out_name = "hidden.png"

def download(url, save_name):
    resp = requests.get(url, stream = True)
    if (resp.status_code == 200):
        with open(save_name, "wb") as f:
            for chunk in resp:
                f.write(chunk)
    return resp.status_code

if (__name__ == "__main__"):
    download(img_url, src_name)
    
    with open(src_name, "rb") as source:
        source.seek(offset)
        with open(out_name, "wb") as out:
            out.write(source.read())
    
    image = Image.open(out_name)
    image.show()