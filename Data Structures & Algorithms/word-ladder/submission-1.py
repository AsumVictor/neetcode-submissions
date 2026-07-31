from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # the length of the words are not only 3
        # using bfs:
        """
        for current word
         - add to visited
         - check if that word exit in target

         - now from 1 - n in curr word:
              for 1 - 26:
                  check if conact of prev and after work in the words:
                  if word not in visted and in word add it.



       
        """
        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        wordList = set(wordList)

        while queue:
            word, count = queue.popleft()
            visited.add(word)

            if word == endWord:
                return count

            
            # mutate them
            for i in range(len(word)):
                for j in range(26):
                    # create a string of len
                    generated = chr(ord("a") + j)
                    new_word = word[:i] + generated + word[i+1:]

                    # check and ad word
                    if (new_word in wordList) and (new_word not in visited):
                        visited.add(new_word)
                        queue.append((new_word, count + 1))
            
        
        return 0
            


        



