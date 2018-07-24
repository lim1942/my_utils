#  pyhton3

def get_cn_first_letter(_str,codec="UTF8"):
    
    _str = _str.encode("GBK")
    
    if _str<b"\xb0\xa1" or _str>b"\xd7\xf9":
        return _str.decode('GBK')
    if _str<b"\xb0\xc4":
        return "a"
    if _str<b"\xb2\xc0":
        return "b"
    if _str<b"\xb4\xed":
        return "c"
    if _str<b"\xb6\xe9":
        return "d"
    if _str<b"\xb7\xa1":
        return "e"
    if _str<b"\xb8\xc0":
        return "f"
    if _str<b"\xb9\xfd":
        return "g"
    if _str<b"\xbb\xf6":
        return "h"
    if _str<b"\xbf\xa5":
        return "j"
    if _str<b"\xc0\xab":
        return "k"
    if _str<b"\xc2\xe7":
        return "l"
    if _str<b"\xc4\xc2":
        return "m"
    if _str<b"\xc5\xb5":
        return "n"
    if _str<b"\xc5\xbd":
        return "o"
    if _str<b"\xc6\xd9":
        return "p"
    if _str<b"\xc8\xba":
        return "q"
    if _str<b"\xc8\xf5":
        return "r"
    if _str<b"\xcb\xf9":
        return "s"
    if _str<b"\xcd\xd9":
        return "t"
    if _str<b"\xce\xf3":
        return "w"
    if _str<b"\xd1\x88":
        return "x"
    if _str<b"\xd4\xd0":
        return "y"
    if _str<b"\xd7\xf9":
        return "z"


def main():

    while 1:
        text = input('Please input a text line ...')
        new_line = ''
        for i in text:
            new_line+=get_cn_first_letter(i)
        print(new_line.replace('-','_')+'_content')


if __name__ == '__main__':
    main()
