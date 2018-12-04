
def line_splitter(filename):
    num1 = []
    with open(filename, encoding="utf8") as text:
        text = text.read()
    text.strip("\n")
    line = text.splitlines()
    
    return line  

def search_cap_letter(line):
    speech_box = []
    speech_box1 = []
    DASH = "—"
    cap_inp = input("Найти речь, начинающуюся с (заглавная буква): ")
    cap_inp.upper()
    if len(cap_inp) == 1:
        cap_letter = cap_inp
    else:
        cap_letter = cap_inp[0]
    for l in line:    
        if l.startswith(DASH)and cap_letter in l:
            speech_box.append(l)
            
    for item in speech_box:
        item = item.strip("— ")
        if item.startswith(cap_letter):
            speech_box1.append(item)
                
    if len(speech_box1) == 0:
        print("Такой буковки нет :(")
    else:
        return "\n".join(speech_box1)

def main():
    line = line_splitter("prilepin.txt")
    print(search_cap_letter(line))
    
    
if __name__ == "__main__":
    main()
