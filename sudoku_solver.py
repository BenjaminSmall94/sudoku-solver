class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        Solution.set_up(board)
        Solution.analytical_solve(board, 8)
        copied_board = [board[i].copy() for i in range(9)]
        Solution.recursive_solve(board, copied_board, 0, 0)

    @staticmethod
    def analytical_solve(board, max_reps):
        reps = 0
        while not Solution.is_solved(board) and reps < max_reps:
            for i in range(9):
                for j in range(9):
                    Solution.examine_cell(board, i, j)
            reps += 1

    @staticmethod
    def recursive_solve(board, copied_board, i , j):
        if isinstance(board[i][j], set):
            possible_nums = board[i][j].copy()
            for num in possible_nums:
                board[i][j] = num
                if Solution.is_valid_cell(board, i, j):
                    if i == 8 and j == 8:
                        return True
                    elif j == 8:
                        if Solution.recursive_solve(board, copied_board, i + 1, 0):
                            return True
                    else:
                        if Solution.recursive_solve(board, copied_board, i, j + 1):
                            return True
            else:
                board[i][j] = copied_board[i][j]
                return False
        else:
            if i == 8 and j == 8:
                return True
            elif j == 8:
                if Solution.recursive_solve(board, copied_board, i + 1, 0):
                    return True
            else:
                if Solution.recursive_solve(board, copied_board, i, j + 1):
                    return True


    @staticmethod
    def is_valid_cell(board, i, j):
        for k in range(9):
            if j == k:
                continue
            if board[i][j] == board[i][k]:
                return False
        for h in range(9):
            if i == h:
                continue
            if board[i][j] == board[h][j]:
                return False
        x_box = i // 3 * 3
        y_box = j // 3 * 3
        for m in range(x_box, x_box + 3):
            for n in range(y_box, y_box + 3):
                if i == m and j == n:
                    continue
                if board[i][j] == (board[m][n]):
                    return False
        return True

    @staticmethod
    def examine_cell(board, i, j):
        if isinstance(board[i][j], set):
            for k in range(9):
                if isinstance(board[i][k], str):
                    board[i][j].discard(board[i][k])
                    if len(board[i][j]) == 1:
                        board[i][j] = board[i][j].pop()
                        return
            for h in range(9):
                if isinstance(board[h][j], str):
                    board[i][j].discard(board[h][j])
                    if len(board[i][j]) == 1:
                        board[i][j] = board[i][j].pop()
                        return
            x_box = i // 3 * 3
            y_box = j // 3 * 3
            for m in range(x_box, x_box + 3):
                for n in range(y_box, y_box + 3):
                    if isinstance(board[m][n], str):
                        board[i][j].discard(board[m][n])
                        if len(board[i][j]) == 1:
                            board[i][j] = board[i][j].pop()
                            return

    @staticmethod
    def set_up(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    board[i][j] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    @staticmethod
    def write_board(board, working_board):
        for i in range(9):
            for j in range(9):
                board[i][j] = str(working_board[i][j])
        return board

    @staticmethod
    def is_solved(working_board):
        for i in range(9):
            for j in range(9):
                if isinstance(working_board[i][j], set):
                    return False
        return True


if __name__ == '__main__':
    test_board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
                  ["7", ".", ".", ".", ".", ".", ".", ".", "."],
                  [".", "2", ".", "1", ".", "9", ".", ".", "."],
                  [".", ".", "7", ".", ".", ".", "2", "4", "."],
                  [".", "6", "4", ".", "1", ".", "5", "9", "."],
                  [".", "9", "8", ".", ".", ".", "3", ".", "."],
                  [".", ".", ".", "8", ".", "3", ".", "2", "."],
                  [".", ".", ".", ".", ".", ".", ".", ".", "6"],
                  [".", ".", ".", "2", "7", "5", "9", ".", "."]]

    # test_board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
    #               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #               [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #               ["7", ".", "."," .", "2", ".", ".", ".", "6"],
    #               [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #               [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    solver = Solution()
    solver.solveSudoku(test_board)
