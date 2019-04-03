import re

def search_text(text):
    
    pattern = "\w*ъ"
    result = re.findall(pattern,text)
    return len(result)
    
    """
    repl = "g<word>"
    new_text = re.sub(pattern, repl, text)
    
def listing_ъ(text, d):
    
    pattern = "\b(?P<word>\w*)ъ\b"
    
    
    for word in line:
        if word not in d.keys():
            d[word] = 1
        else:
            d[word] = d[word] + 1"""
    

def main():
    filename = input("Введите путь к файлу: ")
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    d = {}
    quant = search_text(text)
    

if __name__ == "__main__":
    main()
