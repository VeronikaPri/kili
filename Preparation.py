
def count_sent(filename):
    num1 = []
    with open(filename, encoding="utf8") as text:
        text = text.read()
    line = text.split("\n")
    for l in line:
        a = l.split(".")
        if len(a) == 2:
            num1.append("1")
    percent = round(len(num1) / len(line) * 100)
    
    return percent

def main():
    print("Процентное содержание строк c 1 предложением: ", count_sent("prilepin.txt"), "%")
    
if __name__ == "__main__":
    main()
