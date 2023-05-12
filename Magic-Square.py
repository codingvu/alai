# Magic Square
def generate_magic_square(n):
    magic_square = [[0 for x in range(n)] for y in range(n)]
    # initialize position of 1
    i = n//2
    j = n-1
    # fill the magic square with numbers
    for num in range(1, n**2+1):
        magic_square[i][j] = num
        # find next position
        i -= 1
        j += 1
        # if the next position is out of range
        if i == -1 and j == n:
            j = n-2
            i = 0
        else:
            if i == -1:
                i = n-1
            if j == n:
                j = 0
        # if the next position is already filled
        if magic_square[i][j] != 0:
            j -= 2
            i += 1
        # loop back to top if the next position is out of range
        if j == n:
            j = 0
        if i == -1:
            i = n-1
    return magic_square
def main():
    n = int(input("Enter size of magic square: "))
    magic_square = generate_magic_square(n)
    for row in magic_square:
        print(row)
if __name__ == "__main__":
    main()
