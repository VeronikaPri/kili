import re

def count_lines(filename):
    with open(filename, "r", encoding = "utf-8") as f:
        text = f.read()
    result = re.search("\s+<se>\n(.+?&)\s+</se>", text, flags = re.MULTILINE | re.DOTALL)
    result1 = result.group(1)
    lines = result1.splitlines()
    count = len(lines)
    return count
def main():
    length_of_lines = count_lines("17.xml")
    with open("new.txt", "a", encoding = "utf-8") as t:
        t.write(str(length_of_lines)+ "\n")
if __name__ == '__main__':
    main()
