def funcUpdation(currPassword, newPassword):
    n = len(currPassword)
    m = len(newPassword)

    # Create DP table for LCS
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if currPassword[i - 1] == newPassword[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_len = dp[n][m]

    # Minimum updates = deletions + insertions
    deletions = n - lcs_len
    insertions = m - lcs_len
    return deletions + insertions


def main():
    # input for currPassword
    currPassword = str(input().strip())

    # input for newPassword
    newPassword = str(input().strip())

    result = funcUpdation(currPassword, newPassword)
    print(result)


if __name__ == "__main__":
    main()
