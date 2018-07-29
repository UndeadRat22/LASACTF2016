import re

_input = "Dayq ymk rmxx, ngf yk oubtqd iuxx dqymuz. Fmwq ftue rxms uz dqyqyndmzoq: xmemofr{nq_eturfqp_za_yadq}"

def is_upper(c):
    if (c >= ord('A')) & (c <= ord('Z')):
        return True
    return False
    
def is_lower(c):
    if (c >= ord('a')) & (c <= ord('z')):
        return True
    return False

def shift(text, step):
    output = ""
    for letter in text:
        char = ord(letter)
        if is_lower(char):
            char = ord(letter)+step
            while (char > ord("z")):
                char-=26
        if is_upper(char):
            char = ord(letter)+step
            while (char > ord("Z")):
                char-=26
        output+=chr(char)
    return output

if (__name__ == "__main__"):
    step = 1
    while (step <= 27):
        _out = shift(_input, step)
        flags = re.findall("lasactf{(.*)}", _out)
        if flags:
            print(flags[0])
        step+=1