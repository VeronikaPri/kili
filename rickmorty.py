def get_season_files(season, episode, dataset_dir="./dataset"):
    files = []
    for num in episode:
        filik = dataset_dir + "/" + "season" + str(season) + "/" + "episode" + str(num) + ".txt"
        files.append(filik)
   
    return files

def parse_episode(file):
    cues = []
    name = ''
    with open(file, encoding="utf-8") as fid:
        for line in text:
            line = line.strip(\n):
            if line = "" or (line[0] == "(" and line[-1] == ")") or (line[0] == "[" and line[-1] == "]"):
                continue
            else:
                parts = line.split(":", maxsplit=1)
                if len()parts == 2:
                    name = parts[0]
                frase = parts[-1]
                words = get_words(frase)
                cues.append((name, words))

    return cues
            
            
 def clear_text(text):
    
    trash_symbols = '!"#$%&\'-()*+,./:;<=>?@[\\]^_`{|}~«»—'

    return text.strip(trash_symbols)

def get_words(string_of_text):
    '''Преобразует текст в набор токенов.
        Токеном является слово, очищенное от любых символов, кроме букв.
    '''

    good_words = []

    for word in string_of_text.split():
        candidate = clear_text(word)
        if candidate != '':
            candidate = candidate.lower()
            good_words.append(candidate)
    

def main():
    files = get_season_files(1, [1, 2, 3, 4, 5, 6 , 7, 8, 9 , 10])

    cues = parse_episode(files[0])




"""


    return good_words
"""
