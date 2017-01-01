# simple anagram finder
# if you don't have a dictionary you can download one from:
# https://github.com/dwyl/english-words

class AnagramFinder:

    def __init__(self, keyword, dictionary):
        self.keyword = keyword.strip()
        self.dictionary = dictionary
        self.anagrams = []

    def find(self):
        tokenised_keyword = self.tokenise(self.keyword)
        for word in self.dictionary:
            if self.tokenise(word) == tokenised_keyword:
                self.anagrams.append(word)
        return self.anagrams

    def tokenise(self, target):
        tokens = {}
        for i in range(len(target)):
            if target[i] in tokens:
                tokens[target[i]] += 1
            else:
                tokens[target[i]] = 1
        return tokens

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        sys.stderr.write('Please provide a keyword.\nUsage: ' + sys.argv[0] +
        ': <keyword> [<dictionary>].\n')
        exit(1)
    elif len(sys.argv) == 2:
        dictionary_file = '/usr/share/dict/words'
    else:
        dictionary_file = sys.argv[2]

    stripped_dict = []
    with open(dictionary_file) as dict:
        for line in dict.readlines():
            stripped_dict.append(line.strip())

    af = AnagramFinder(sys.argv[1], stripped_dict)
    for anagram in af.find():
        print anagram
