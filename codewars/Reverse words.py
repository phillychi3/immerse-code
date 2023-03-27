def reverse_words(text):
    str = []
    for i in text.split(" "):
        str.append(i[::-1]) 
    return ' '.join(str)