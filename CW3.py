import re
from collections import Counter

def words_finder(filename):
    with open(filename, "r", encoding = "utf-8") as f:
        text = f.read()
        
    result = re.findall('.+?<ana gr="([A-Z=]+),.*?" lex="(.+?)"/>', text, flags = re.MULTILINE | re.DOTALL)
    pos_map = {}
    for pos, lex in result:
        if pos not in pos_map:
            pos_map[pos] = []
        pos_map[pos].append(lex)
    for pos, lemmas in pos_map.items():
        with open(pos + ".txt", "a", encoding ='utf-8') as txt:
            txt.write("\n".join(lemmas) + "\n")
    return 

def main():
    
    result = words_finder("17.xml")
        
if __name__ == '__main__':
    main()
