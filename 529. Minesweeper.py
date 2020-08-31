from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        pass


board = [['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'M', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E']]

click = [3, 0]

update_board = Solution().updateBoard(board, click)

print(update_board)
