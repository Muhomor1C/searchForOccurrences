import os
import re


def read_file(file, main_file):
    pattern = re.compile(';|,| |:|. |\\(|\\)|\\t|\\n|\\r')
    with open(file, 'r', encoding="utf-8") as file:
        file = file.read()
        if main_file:
            return pattern.split(file)
        else:
            for word in search_words:
                search_words[word] += pattern.split(file).count(word)


def search_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            list_of_files.append(os.path.join(root, file))
    return list_of_files


def search():
    for file in list_of_files:
        read_file(file, False)
    return search_words


if __name__ == '__main__':
    sample = './words.txt'
    directoryes = ('./files', './files1', './files2')
    search_words = dict.fromkeys(set(read_file(sample, True)), 0)
    list_of_files = []
    for directory in directoryes:
        list_of_files = search_files(directory)
    print(search())
