class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowhash = set()
            colhash = set()
            gridhash = set()
            for j in range(9):

                if board[i][j] != ".":
                    if not board[i][j] in rowhash:
                        rowhash.add(board[i][j])
                    else:
                        return False

                if board[j][i] != ".":
                    if not board[j][i] in colhash:
                        colhash.add(board[j][i])
                    else:
                        return False

                row = (j // 3) + 3*(i // 3)
                col = (j % 3) + 3*(i % 3)
                if board[row][col] != ".":
                    if not board[row][col] in gridhash:
                        gridhash.add(board[row][col])
                    else:
                        return False

                
        return True