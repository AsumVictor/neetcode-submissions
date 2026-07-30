class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        n = len(word)
        index = 0
        while index < n:
            # if the char is in trie
            if word[index] in trie:
                # the the trie to that work and call the next char
                trie = trie[word[index]]
            else:
                trie[word[index]] = {}
                trie = trie[word[index]]
            
            index += 1
        trie["."] = {}

    def search(self, word: str) -> bool:
        trie = self.trie
        n = len(word)
        index = 0

        while index < n:
            if not (word[index] in trie):
                return False

            trie = trie[word[index]]
            index += 1

        return "." in trie

        
        

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        n = len(prefix)
        index = 0

        while index < n:
            if not (prefix[index] in trie):
                return False

            trie = trie[prefix[index]]
            index += 1

        return True


