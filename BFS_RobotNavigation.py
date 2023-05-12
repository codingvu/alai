import copy
from colorama import Fore, init

init(autoreset=True)


class Robot:
    table = [
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        [
            "-",
            Fore.YELLOW + "#",
            "-",
            "-",
            "-",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            "-",
        ],
        [
            "-",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            Fore.YELLOW + "#",
            "-",
        ],
        [
            "-",
            "-",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            Fore.YELLOW + "#",
            "-",
        ],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ]
    goalX = 6
    goalY = 2
    startX = 0
    startY = 3
    newTable = copy.deepcopy(table)
    queue = []
    visited = []

    def calcManhatten(self):
        self.table[self.startY][self.startX] = Fore.BLUE + "S"
        self.table[self.goalY][self.goalX] = Fore.RED + "G"
        print("\n Manhatten Distance: \n")
        for i in range(5):
            for j in range(11):
                if self.table[i][j] != Fore.YELLOW + "#":
                    self.newTable[i][j] = str(
                        abs(self.goalX - j) + abs(self.goalY - i))
                print("\t", self.newTable[i][j], end="")
               
            print("\n")
        position = [self.startX, self.startY]
        self.queue.append((self.newTable[self.startY][self.startX], position))

    def getNeighbors(self):
        position = [[0] * 2] * 4
        value = ["0"] * 4
        position[0] = [self.startX + 1, self.startY]
        position[1] = [self.startX - 1, self.startY]
        position[2] = [self.startX, self.startY - 1]
        position[3] = [self.startX, self.startY + 1]
        for i in range(4):
            if (
                position[i][1] > -1
                and position[i][1] < 5
                and position[i][0] > -1
                and position[i][0] < 11
            ):
                value[i] = self.newTable[position[i][1]][position[i][0]]
                if value[i] != Fore.YELLOW + "#" and (
                    (value[i], position[i]) not in self.visited
                ):
                    self.queue.append((value[i], position[i]))
        self.queue.sort(reverse=True)

    def bestfirstsearch(self):
        steps = 0
        while self.queue:
            input()
            print(f"Steps taken: {steps}")
            print(f"Queue: {self.queue}")
            next = self.queue.pop()
            print(f"Selecting: {next}")
            print(f"Current queue: {self.queue}")
            if next[1][0] == self.goalX and next[1][1] == self.goalY:
                print(f"Goal State reached in {steps} steps")
                exit(1)
            if next[1] == [self.startX, self.startY]:
                self.table[next[1][1]][next[1][0]] = Fore.BLUE + "S"
            else:
                self.table[next[1][1]][next[1][0]] = Fore.GREEN + str(next[0])
            self.visited.append(next)
            self.startX = next[1][0]
            self.startY = next[1][1]
            self.getNeighbors()
            print(
                f"Adding neighbours of {next} to queue\nCurrent queue:{self.queue}\n")
            self.printTable(self.table)
            print(
                "\t---------------------------------------------------------------------------------"
            )
            steps += 1

    def printTable(self, table):
        for i in range(5):
            for j in range(11):
                print("\t" + Fore.WHITE + table[i][j], end="")
            print("\n")


s = Robot()
s.calcManhatten()
print("\n Current State:")
s.printTable(s.table)
s.bestfirstsearch()
