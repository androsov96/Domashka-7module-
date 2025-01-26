class WordsFinder:
    def __init__(self, *names_file):
        self.file_names = list(names_file)

    def get_all_words(self):
        all_words = {}
        list_words = []
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip().lower().translate(str.maketrans('', '', ",.=!?:;-"))
                    word = line.split()
                    for i in word:
                        list_words.append(i)
                all_words[file_name] = list_words
            return all_words

    def find(self, word):
        self.get_all_words()
        result = {}
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.index(word.lower()) + 1
        return result

    def count(self, word):
        self.get_all_words()
        result = {}
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word.lower())
        return result

finder2 = WordsFinder("test_file.txt")
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))