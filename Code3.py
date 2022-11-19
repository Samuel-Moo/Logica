'''Check if the text is a palindrom or not '''
def convert_text(text):
    text = text.lower()
    text = text.split()
    text = ''.join(text)
    return text

def check_palindrom(text):
    t = convert_text(text)
    reverse_t = convert_text(text[::-1])

    if t == reverse_t:
        return True
    else:
        return False

if __name__ == '__main__':
    text1 = "Anita lava la tina"
    text2 = "este es un ejemplo"
    
    print(check_palindrom(text1))
    print(check_palindrom(text2))