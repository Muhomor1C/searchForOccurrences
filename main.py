import os
import re


def read_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        words = file.read()
    return re.split(';|,| |:|. |\\(|\\)|\\t|\\n|\\r', words)


def search_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            list_of_files.append(os.path.join(root, file))
    return list_of_files


def search():
    search_words = dict.fromkeys(set(read_file(filename)), 0)
    for file in list_of_files:
        words_in_file = read_file(file)
        for word in search_words:
            search_words[word] = search_words[word] + words_in_file.count(word)
    return search_words


if __name__ == '__main__':
    filename = './words.txt'
    directoryes = ('./files', './files1', './files2')
    list_of_files = []
    for directory in directoryes:
        list_of_files = search_files(directory)
    print(search())
