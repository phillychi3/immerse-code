import re
def to_camel_case(text):
    text = re.split(r'[-_]',text)
    rt = ''
    for i in range(len(text)):
        if i == 0:
            rt += text[i]
        else:
            rt += text[i].capitalize()
    
    return rt