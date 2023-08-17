import re
CYRILLIC_SYMBOLS = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "je", "zh", "z", "y", "i", "ji", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "ju", "ja")
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper() 
def normalize(name):
    name_extension = name.split('.')
    extension = name_extension[-1]
    name = ".".join(name_extension[:-1:])
    new_name = name.translate(TRANS)
    new_name = re.sub('\W - .', '_', new_name)
    return f"{new_name}.{extension}"
