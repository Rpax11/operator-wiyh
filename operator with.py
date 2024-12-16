import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    text = f.read().lower()
                    text = re.sub(r'[^\w\s-]', '', text)
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл '{file_name}' не найден.")
            except Exception as e:
                print(f"Ошибка при обработке файла '{file_name}': {e}")
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words_dict = self.get_all_words()
        for filename, words in all_words_dict.items():
            try:
                index = words.index(word)
                result[filename] = index + 1
            except ValueError:
                result[filename] = None
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words_dict = self.get_all_words()
        for filename, words in all_words_dict.items():
            result[filename] = words.count(word)
        return result

finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('text'))
print(finder.count('text'))