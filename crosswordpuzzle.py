def printMatrix(matrix, n):
    for i in range(n):
        print(matrix[i])
    print()


def checkHorizontal(x, y, matrix, currentWord):
    n = len(currentWord)
    for i in range(n):
        if matrix[x][y + i] == "#" or matrix[x][y + i] == currentWord[i]:
            matrix[x] = matrix[x][:y + i] + \
                currentWord[i] + matrix[x][y + i + 1:]
        else:
            matrix[0] = "@"
            return matrix
    return matrix


def checkVertical(x, y, matrix, currentWord):
    n = len(currentWord)
    for i in range(n):
        if matrix[x + i][y] == "#" or matrix[x + i][y] == currentWord[i]:
            matrix[x + i] = matrix[x + i][:y] + \
                currentWord[i] + matrix[x + i][y + 1:]
        else:
            matrix[0] = "@"
            return matrix
    return matrix


def solvePuzzle(words, matrix, index, n):
    if index < len(words):
        currentWord = words[index]
        maxLen = n - len(currentWord)
        for i in range(n):
            for j in range(maxLen + 1):
                temp = checkVertical(j, i, matrix.copy(), currentWord)
                if temp[0] != "@":
                    solvePuzzle(words, temp, index + 1, n)
        for i in range(n):
            for j in range(maxLen + 1):
                temp = checkHorizontal(i, j, matrix.copy(), currentWord)
                if temp[0] != "@":
                    solvePuzzle(words, temp, index + 1, n)
    else:
        printMatrix(matrix, n)
        print()


if __name__ == "__main__":
    n1 = 10
    matrix = []
    words = []
    matrix.append("*#********")
    matrix.append("*#********")
    matrix.append("*#****#***")
    matrix.append("*##***##**")
    matrix.append("*#****#***")
    matrix.append("*#****#***")
    matrix.append("*#****#***")
    matrix.append("*#*######*")
    matrix.append("*#********")
    matrix.append("***#######")
    words.append("PUNJAB")
    words.append("JHARKHAND")
    words.append("MIZORAM")
    words.append("MUMBAI")
    solvePuzzle(words, matrix, 0, n1)
