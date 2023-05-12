#Cryptarithmetic
from colorama import Fore, init
init(strip=False)
init(autoreset=True)
class Cryptarithmetic():
    def __init__(self):
        self.is_solved = False
        self.solution_count = 0
    def start(self):
        word1 = input("Enter First Word - ").upper()
        word2 = input("Enter Second Word - ").upper()
        result = input("Enter Result - ").upper()
        values = []
        visited = [False for _ in range(10)]
        equation = [word1, word2, result]
        # Get Unique Letters
        unique_letters = list(set(word1 + word2 + result))
        if len(unique_letters) > 10:
            print("\nNo Solution (as values will repeat)\n")
            exit()
        print("Solution Is - ")
        print(f" \t{word1}\n+\t{word2}\n-------------\n\t{result}\n\n")
        self.solve(unique_letters, values, visited, equation)
    def solve(self, letters, values, visited, equation):
        if len(letters) == len(values):
            letter_value_map = {letter: value for letter,
                                value in zip(letters, values)}
            if letter_value_map[equation[0][0]] == 0 or letter_value_map[equation[1][0]] == 0 or letter_value_map[equation[2][0]] == 0:
                return
            word1 = ''.join(str(letter_value_map[c]) for c in equation[0])
            word2 = ''.join(str(letter_value_map[c]) for c in equation[1])
            res = ''.join(str(letter_value_map[c]) for c in equation[2])
            if int(word1) + int(word2) == int(res):
                self.solution_count += 1
                print(
                    Fore.GREEN + f"Result {self.solution_count} = {word1} + {word2} = {res}\n")
                self.is_solved = True
            return
        for i in range(10):
            if not visited[i]:
                visited[i] = True
                values.append(i)
                self.solve(letters, values, visited, equation)
                values.pop()
                visited[i] = False
temp = Cryptarithmetic()
temp.start()
