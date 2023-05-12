from copy import deepcopy
from colorama import init

init(autoreset=True)


class Puzzle:
    board = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    startX = 0
    startY = 0
    queue = []
    generatedBoards = []

    def calcHeuristic(self, board):
        h = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] != self.goal[i][j]:
                    h = h + 1
        return h - 1

    def getValidMoves(self, board):
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    self.startX = j
                    self.startY = i
        position = [[0] * 2] * 4
        validMoves = []
        position[0] = [self.startX + 1, self.startY]
        position[1] = [self.startX - 1, self.startY]
        position[2] = [self.startX, self.startY - 1]
        position[3] = [self.startX, self.startY + 1]
        for i in range(4):
            if (
                position[i][1] > -1
                and position[i][1] < 3
                and position[i][0] > -1
                and position[i][0] < 3
            ):
                validMoves.append(position[i])
        return validMoves

    def playMove(self, move: list, board: list):
        newBoard = deepcopy(board)
        temp = newBoard[move[1]][move[0]]
        newBoard[move[1]][move[0]] = newBoard[self.startY][self.startX]
        newBoard[self.startY][self.startX] = temp
        return newBoard

    def astar(self):
        self.calcHeuristic(self.board)
        self.queue.append((self.calcHeuristic(self.board), self.board))
        self.generatedBoards.append(self.board)
        i = 0
        while i < 1000:
            next = self.queue.pop()
            moves = self.getValidMoves(next[1])
            print("\n---------------\n")
            print(f" step {i}\n")
            for j in range(3):
                print(" ", next[1][j])
            if next[1] == self.goal:
                print(f"\nGoal state reached in {i} steps")
                print("\n------------------------------\n")
                exit(1)
            for move in moves:
                newBoard = self.playMove(move, next[1])
                if newBoard not in self.generatedBoards:
                    self.generatedBoards.append(newBoard)
                    self.queue.append((self.calcHeuristic(newBoard), newBoard))
                    self.queue.sort(reverse=True)
            i += 1
        return None


print("8-Puzzle Problem\n")
temp = Puzzle()
temp.astar()
