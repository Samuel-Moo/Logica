def convert_text(text):
     text = text.lower()
     text = text.split()
     text = ''.join(text)
     return text


def check_palindorm(text):
    t = convert_text(text)
    reverse_t = convert_text(text[::-1])

    if t == reverse_t:
        return True
    else:
        return False 


if __name__ == '__main__': 
    text1 = "Juanauj"
    text2 = "eefneifnaonef"

    print(check_palindorm(text1))
    print(check_palindorm(text2))