import os
import re

sample = './words.txt'  # Слова, которые надо найти находятся в файле образце
directoryes = ['./files', './files1', './files2']  # Где ищем файлы
pattern = re.compile(';|,| |:|. |\\(|\\)|\\t|\\n|\\r')  # Шаблон с разделителями


def read_file(file, word):
    with open(file, 'r', encoding="utf-8") as file:
        file = file.read()
        if word:
            return pattern.split(file).count(word)
        else:
            return pattern.split(file)


def find_word(directoryes):
    for directory in directoryes:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file = os.path.join(root, file)
                for word in search_words:
                    search_words[word] += read_file(file, word)
    return search_words


if __name__ == '__main__':
    search_words = dict.fromkeys(set(read_file(sample, '')), 0)
    print(find_word(directoryes))
