import os
import re

sample = './words.txt'  # Слова, которые надо найти находятся в файле образце
directoryes = ['./files', './files1', './files2']  # Где ищем файлы
list_of_files = []  # Список с файлами. Заполняется автоматически
pattern = re.compile(';|,| |:|. |\\(|\\)|\\t|\\n|\\r')  # Шаблон с разделителями


def read_file(file: str, main_file: bool):
    """
        Получает имя файла и признак "файла образца для поиска".
    Если это файл образец, то читает его содержимое и возвращает список слов для
    поиска. Иначе добавляет в словарь search_words количество найденных слов.
        Здесь нарушен принцип единственной ответственности, но если делать по
    другому, то придется либо передавать открытый файл или, того хуже, список,
    из функции в функцию, что скажется на производительности, либо делать две функции,
    которые будут открывать файл, что, в свою очередь, нарушает принцип
    "Не повторяй себя". Увы, лучше не придумал. Все ради производительности.
    :param file: str - имя и путь к файлу
    :param main_file: bool - признак файла образца
    :return: list - search_words - если main_file == True - список слов для поиска
    """

    with open(file, 'r', encoding="utf-8") as file:
        file = file.read()
        if main_file:
            return pattern.split(file)
        else:
            for word in search_words:
                search_words[word] += pattern.split(file).count(word)


def search_files():
    for directory in directoryes:
        for root, dirs, files in os.walk(directory):
            for file in files:
                list_of_files.append(os.path.join(root, file))


def search():
    for file in list_of_files:
        read_file(file=file, main_file=False)
    return search_words


if __name__ == '__main__':
    search_words = dict.fromkeys(set(read_file(file=sample, main_file=True)), 0)
    search_files()
    print(search())