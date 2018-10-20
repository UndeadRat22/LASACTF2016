encryptedMessage = "69,14,93,71,28,91,9,30,18,16,18,75,71,14,90,14,9,18,20,18,87,2,10,21,20,90,69,8,21,94,71,13,83,20,90,64,2,30,9,71,27,92,3,90,70,15,31,18,23,8,91,29,31,18,16,27,65,71,27,69,6,8,86,2,30,18,19,21,18,6,90,94,2,27,64,9,31,86,71,23,83,9,90,93,1,90,70,15,31,18,41,21,64,19,18,30,71,13,90,8,90,86,2,23,93,9,9,70,21,27,70,2,30,18,5,3,18,38,90,66,11,15,65,71,56,18,10,19,92,18,9,18,36,90,86,14,12,91,3,31,86,71,24,75,71,32,30,71,14,90,6,14,18,19,18,87,71,9,90,2,31,66,71,23,71,20,14,18,5,31,18,21,31,86,75,90,83,9,30,18,3,19,87,71,21,84,71,14,90,2,90,64,8,14,28,69,90,31,71,22,83,20,27,81,19,28,73,46,37,94,14,17,87,56,25,83,9,30,91,3,31,109,20,18,87,2,10,79"

# 3
# A B C
# A A A
# A A B
# A A A
# B A A
# C A A
# D A A
# [0 - 256] -> [++] if[256] [0] -> [++] if [256] -> ret None
def iter_keys():
    keyTuple = [0, 0, 0]
    while (True):
        keyTuple[0] += 1
        if (keyTuple[0] >= 256):
            keyTuple[0] = 0
            keyTuple[1] += 1
        if (keyTuple[1] >= 256):
            keyTuple[1] = 0
            keyTuple[2] += 1
        if (keyTuple[2] == 255):
            yield keyTuple
            break
        yield keyTuple

def get_bytes(msg):
    bytes = []
    for num in msg.split(","):
        bytes.append(int(num))
    return bytes

def xor_key(msg, key):
    deciphered = []
    key_ptr = 0
    key_len = len(key)
    for byte in msg:
        xored_byte = key[key_ptr] ^ byte
        key_ptr += 1
        if key_ptr >= key_len:
            key_ptr = 0
        deciphered.append(xored_byte)
    return deciphered

def convert_to_str(byte_list):
    str = ""
    for byte in byte_list:
        str += chr(byte)
    return str

if __name__ == "__main__":
    l = get_bytes(encryptedMessage)
    generator = iter_keys()
    for key in generator:
        byte_text = xor_key(l, key)
        str = convert_to_str(byte_text)
        if "lasactf" in str:
            print(str)
            print(key)
            break
    print("failed")

#out:
# "to find why this sheep's wool was red; and the prize was awarded to a learned man of the North, who demonstrated by A plus B minus C divided by Z, that the sheep must be red, and die of the rot." - lasactf{I_like_candide_sheep}
#[103, 122, 50]
#or in ascii: gz2 :----DDDD