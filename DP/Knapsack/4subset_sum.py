"""
Given a list and sum find if there is a subset whose sum is equal to the
provided sum.

Returns True / False
"""


def subset_sum(arr, sum, l):

    t = [[False for i in range(sum + 1)] for i in range(l + 1)]

    for i in range(l + 1):
        t[i][0] = True

    for i in range(sum + 1):
        t[0][i] = False

    for i in range(1, l + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    return t[l][sum]


def main():
    arr = []

    sum = int(input("Enter Sum: "))
    l = int(input("Enter size of input: "))

    for i in range(0, l):
        a = int(input("Integer: "))
        arr.append(a)

    print(subset_sum(arr, sum, l))


if __name__ == "__main__":
    main()
