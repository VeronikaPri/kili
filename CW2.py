import re
from collections import Counter

def gram_things(filename):
    with open(filename, "r", encoding = "utf-8") as f:
        text = f.read()
        
    result = re.findall('.+?<ana gr="(.+?)".+?>', text, flags = re.MULTILINE | re.DOTALL)
    dict_of_gram = Counter(result)
    
    return dict_of_gram

def main():
    dictionary = gram_things("17.xml")
    with open("new.txt", "a", encoding = "utf-8") as t:
        for key, value in dictionary.most_common():
            t.write(key)
            t.write(" - ")
            t.write(str(value))
            t.write("\n")
        
if __name__ == '__main__':
    main()
