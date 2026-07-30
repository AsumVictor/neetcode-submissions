class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
       """
       for frist wor i = 0

       ["A","B","C","E"]
       ["S","F","C","S"]
       ["A","D","E","E"]

        i = len(words): reach the words
        True

        grid i not same word i
         False

        if i,j are out of bouns
           i < row or > row
           j is < col or > col

        
        visited:
         chnages it

        up: i + 1, j
        downl: i -1 , j

        left: i, j - 1
        right: i, j + 1

        undo
        change back to orginal

        return result or this

       """
       col = len(board[0])
       row = len(board)
       n = len(word)

       def search(i, j, idx):
        
        # check boundries
        if i < 0 or i > row - 1 or j < 0 or j > col - 1 or idx > n - 1:
            return False

        # check feasibility
        board_char = board[i][j]
        word_char = word[idx]

        if idx == n - 1 and word_char ==  board_char:
            return True

        # check for 
        if word_char != board_char:
            return False

        board[i][j] = "#"

        # explore neibords
        # up
        up = search(i - 1, j, idx + 1)
        # down
        down = search(i + 1, j, idx + 1)
        # left
        left = search(i, j - 1, idx + 1)
        #right
        right = search(i, j + 1, idx + 1)

        board[i][j] = board_char

        return up or down or left or right

    
       for i in range(len(board)):
         for j in range(len(board[0])):
            if search(i, j, 0):
                return True

       return False

        
