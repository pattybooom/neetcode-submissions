class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #check rows 
        rows = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] in rows and board[i][j] != ".":
                    return False
                rows.add(board[i][j])
            rows = set()

        #check columns 

        columns = set()
        for i in range(9):
            for j in range(9):
                if board[j][i] in columns and board[j][i] != ".":
                    return False
                columns.add(board[j][i])
            columns = set()



        #check boxes

        midi_values = [1,4,7]
        midj_values = [1,4,7]
        midi = 0
        midj = 0

        #we need to check for each combo od mid values 
        for midi in midi_values:
            for midj in midj_values:
                boxes = set()
                # collect all 9 cells around each midpoint (3x3 box)
                for i in range(midi - 1, midi + 2):  # e.g., 0–2, 3–5, 6–8
                    for j in range(midj - 1, midj + 2):
                        if board[i][j] != ".":
                            if board[i][j] in boxes:
                                return False
                            boxes.add(board[i][j])

        return True
