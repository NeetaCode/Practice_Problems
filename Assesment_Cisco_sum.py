def funcSum(list1, list2):
    i = 0
    j = 0
    carry = 0
    result = []

    # Add digit by digit
    while i < len(list1) or j < len(list2) or carry:
        d1 = list1[i] if i < len(list1) else 0
        d2 = list2[j] if j < len(list2) else 0

        total = d1 + d2 + carry
        result.append(total % 10)
        carry = total // 10

        i += 1
        j += 1

    return result


def main():
    # input-for-list1
    list1_size = int(input())
    list1 = list(map(int, input().split()))

    # input-for-list2
    list2_size = int(input())
    list2 = list(map(int, input().split()))

    result = funcSum(list1, list2)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
