#Подготовка к к.р.
text = "«наивный» - <есть> натуральный, природный, не обработанный искусственными условностями цивилизации. Так что если наша культура есть продолжение природы, её язык (по распространенному мнению философов), её заявление о себе, то в наивном человеке и его слове - это прямейше, спонтанно, без опосредованных звеньев...  — Георгий Гачев, «Плюсы и минусы наивного философствования»"
def clear_text(text, trash_tokens):
#left side clearing 
    text = text.rstrip(trash_tokens)
    return text
def get_words(text):
    trash_tokens = ",.//—-?!()*&^%$#@+=_<>[]«»"
    tokens = text.split()
    good_tokens = []
    for token in tokens:
        clean_token = clear_text(token, trash_tokens)
        if clean_token != "":
            clean_token = clean_token.lower()
            good_tokens.append(clean_token)
    return good_tokens

def find_quotes(input_word, al_quotes, all_quotes_words):
result = []
    for i, quote in ennumerate(all_quotes):
        if input_word in all_quotes_words[i]:
            result.append(quote)
    return result

def main():
    
    filename ="C:\\Users\\student\\Desktop\\textik.txt"
DASH = "—"
    all_quotes = []
    all_quotes_words = []
    
    with open(filename, encoding="utf8") as fid:
        for line in fid:
            line = line.strip()
            parts = line.split(DASH)
            quote = parts[0].strip()
            quote_words = get_words(quote)

            all_quates.append(quote)
            all_quotes_words.append(quote_words)

    while True:
        input_word = input("ведите слово: ")
        if input_word == '':
            break
        input_word = nput
            if "разум" in quote_words:
                list_of_authors.append(author)
                
    print("Слово 'разум' содержится в ",
          len(list_of_authors),
          " цитате(ах)")
    print(", ".join(list_of_authors))

if __name__ == "__main__":
    main()



