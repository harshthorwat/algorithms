def knapsack(wt, val, w, l, arr):
    if l == -1 or w == 0:
        return 0
    if arr[l][w] != -1:
        return arr[l][w]
    else:
        return max(
            val[l] + knapsack(wt, val, w - wt[l], l - 1, arr),
            knapsack(wt, val, w, l - 1, arr),
        )


def main():
    wt = []
    val = []

    w = int(input("Enter weight of the knapsack: "))
    l = int(input("Enter size of input: "))

    for i in range(0, l):
        ewt = int(input("weight: "))
        evl = int(input("Value: "))

        wt.append(ewt)
        val.append(evl)

    arr = [[-1] * (w + 1)] * (l + 1)

    print(knapsack(wt, val, w, l - 1, arr))


if __name__ == "__main__":
    main()
