def funcZigZag(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    # Traverse all diagonals
    for d in range(rows + cols - 1):
        temp = []
        r = 0 if d < cols else d - cols + 1
        c = d if d < cols else cols - 1

        while r < rows and c >= 0:
            temp.append(matrix[r][c])
            r += 1
            c -= 1

        if d % 2 == 0:
            temp.reverse()

        result.extend(temp)

    # Return space-separated integers as a string
    return " ".join(map(str, result))


def main():
    matrix_rows, matrix_cols = map(int, input().split())
    matrix = []
    for _ in range(matrix_rows):
        matrix.append(list(map(int, input().split())))

    result = funcZigZag(matrix)
    print(result)


if __name__ == "__main__":
    main()
